# from jose import jwt, JWTError
# from fastapi import Depends, HTTPException
# from fastapi.security import OAuth2PasswordBearer
# from app.core.config import settings

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")



# def get_current_user(token: str = Depends(oauth2_scheme)):

#     try:
#         payload = jwt.decode(
#             token,
#             settings.SECRET_KEY,
#             algorithms=[settings.ALGORITHM]
#         )

#         email = payload.get("sub")

#         if email is None:
#             raise HTTPException(status_code=401, detail="Invalid token")

#         return email

#     except JWTError:
#         raise HTTPException(status_code=401, detail="Invalid token")
    

# from jose import jwt, JWTError

# from fastapi import (
#     Depends,
#     HTTPException
# )

# from fastapi.security import (
#     HTTPBearer,
#     HTTPAuthorizationCredentials
# )

# from app.core.config import settings


# security = HTTPBearer()


# def get_current_user(

#     credentials: HTTPAuthorizationCredentials = Depends(security)

# ):

#     token = credentials.credentials

#     try:

#         payload = jwt.decode(
#             token,
#             settings.SECRET_KEY,
#             algorithms=[settings.ALGORITHM]
#         )

#         email = payload.get("sub")

#         if email is None:

#             raise HTTPException(
#                 status_code=401,
#                 detail="Invalid token"
#             )

#         return email

#     except JWTError:

#         raise HTTPException(
#             status_code=401,
#             detail="Invalid token"
#         )
    

from jose import jwt, JWTError

from fastapi import (
    Depends,
    HTTPException
)

from fastapi.security import (
    HTTPBearer,
    HTTPAuthorizationCredentials
)

from app.core.config import settings


security = HTTPBearer()


def get_current_user(

    credentials: HTTPAuthorizationCredentials = Depends(security)

):

    token = credentials.credentials

    try:

        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM]
        )

        email = payload.get("sub")

        if email is None:

            raise HTTPException(
                status_code=401,
                detail="Invalid token"
            )

        return email

    except JWTError:

        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )

        