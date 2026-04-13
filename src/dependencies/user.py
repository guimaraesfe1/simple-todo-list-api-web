from typing import Annotated

import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jwt.exceptions import InvalidTokenError
from sqlalchemy.exc import NoResultFound

from src.dependencies.session import GetSession
from src.models.user import User
from src.service.user import UserService
from src.utils.jwt_env import jwt_env
from src.utils.hash import verify_password


def get_user_service(session: GetSession):
    return UserService(session)


GetUserService = Annotated[UserService, Depends(get_user_service)]


def get_auth_user(
    user_service: GetUserService,
    user_data: OAuth2PasswordRequestForm = Depends(),
) -> User:
    try:
        user = user_service.get_user_by_email(user_data.username)
    except NoResultFound:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='Invalid Credentials'
        )

    if not verify_password(user_data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='Invalid Credentials'
        )

    return user


GetAuthUser = Annotated[User, Depends(get_auth_user)]

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/api/v1/user/sign-in')

GetToken = Annotated[str, Depends(oauth2_scheme)]

credentials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail='Could not validate credentials',
    headers={'WWW-Authenticate': 'Bearer'},
)


def get_current_user(token: GetToken, user_service: GetUserService):
    try:
        payload = jwt.decode(
            token, jwt_env.SECRET_KEY, algorithms=[jwt_env.ALGORITHM]
        )
        user_id = payload.get('sub')

        if not user_id:
            raise credentials_exception

    except InvalidTokenError:
        raise credentials_exception

    try:
        user = user_service.get_user_by_id(user_id)
    except NoResultFound:
        raise credentials_exception

    return user


GetCurrentUser = Annotated[User, Depends(get_current_user)]
