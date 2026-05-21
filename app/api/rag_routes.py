# from fastapi import APIRouter, Depends

# from app.schemas.rag_schema import QuestionRequest
# from app.services.rag_service import RagService
# from app.core.auth_dependency import get_current_user

# router = APIRouter(prefix="/rag", tags=["RAG APIs"])


# @router.post("/ask")
# def ask_question(
#     payload: QuestionRequest,
#     user=Depends(get_current_user)
# ):

#     result = RagService.ask_question(payload.question)

#     return {
#         "user": user,
#         "answer": result
#     }

# from fastapi import (
#     APIRouter,
#     Depends,
#     UploadFile,
#     File,
#     Form,
#     HTTPException
# )

# import os
# import shutil

# from app.services.rag_service import RagService
# from app.core.auth_dependency import get_current_user

# router = APIRouter(
#     prefix="/rag",
#     tags=["RAG APIs"]
# )

# UPLOAD_DIR = "uploaded_files"

# os.makedirs(UPLOAD_DIR, exist_ok=True)


# # Upload PDF Endpoint
# @router.post("/upload")
# async def upload_pdf(

#     file: UploadFile = File(...),

#     user=Depends(get_current_user)

# ):

#     # Validate PDF
#     if not file.filename.endswith(".pdf"):

#         raise HTTPException(
#             status_code=400,
#             detail="Only PDF files are allowed"
#         )

#     # Save PDF
#     file_path = os.path.join(
#         UPLOAD_DIR,
#         file.filename
#     )

#     with open(file_path, "wb") as buffer:
#         shutil.copyfileobj(file.file, buffer)

#     # Create embeddings
#     RagService.create_vector_store(file_path)

#     return {
#         "message": "PDF uploaded successfully",
#         "filename": file.filename,
#         "uploaded_by": user
#     }


# # Ask Question Endpoint
# @router.post("/ask")
# async def ask_question(

#     question: str = Form(...),

#     user=Depends(get_current_user)

# ):

#     result = RagService.ask_question(question)

#     return {
#         "question": question,
#         "answer": result,
#         "user": user
#     }




#----------------------------------------------
from fastapi import (
    APIRouter,
    Depends,
    UploadFile,
    File,
    Form,
    HTTPException
)

import os
import shutil

from app.services.rag_service import RagService
from app.core.auth_dependency import get_current_user


router = APIRouter(
    prefix="/rag",
    tags=["RAG APIs"]
)


UPLOAD_DIR = "uploaded_files"

os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/upload")
async def upload_pdf(

    file: UploadFile = File(...),

    user=Depends(get_current_user)

):

    if not file.filename.endswith(".pdf"):

        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed"
        )

    file_path = os.path.join(
        UPLOAD_DIR,
        file.filename
    )

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    RagService.create_vector_store(file_path)

    return {
        "message": "PDF uploaded successfully",
        "filename": file.filename,
        "uploaded_by": user
    }


@router.post("/ask")
async def ask_question(

    question: str = Form(...),

    user=Depends(get_current_user)

):

    result = RagService.ask_question(question)

    return {
        "question": question,
        "answer": result,
        "user": user
    }