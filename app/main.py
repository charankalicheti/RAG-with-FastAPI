# from fastapi import FastAPI

# from app.api.auth_routes import router as auth_router
# from app.api.rag_routes import router as rag_router
# from app.api.health_routes import router as health_router

# from app.core.database import Base, engine

# Base.metadata.create_all(bind=engine)

# app = FastAPI(
#     title="Production RAG API",
#     version="1.0.0"
# )

# app.include_router(auth_router)
# app.include_router(rag_router)
# app.include_router(health_router)


from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from app.api.auth_routes import router as auth_router
from app.api.rag_routes import router as rag_router
from app.api.health_routes import router as health_router

from app.core.database import Base, engine

from app.middleware.logging_middleware import LoggingMiddleware


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Production RAG API",
    version="1.0.0"
)


# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Logging Middleware
app.add_middleware(LoggingMiddleware)


# Routers
app.include_router(auth_router)
app.include_router(rag_router)
app.include_router(health_router)