from datetime import timedelta

from fastapi import APIRouter, HTTPException, status
from sqlalchemy.exc import IntegrityError

from src.dependencies.user import GetAuthUser, GetUserService
from src.schemas.auth import CreateToken
from src.schemas.user import SignUpUserSchema
from src.utils.jwt_env import jwt_env
from src.utils.token import create_access_token

router = APIRouter(prefix='/user', tags=['Account Operations'])


@router.post('/sign-up')
def signup_user(user_data: SignUpUserSchema, user_service: GetUserService):

    try:
        user = user_service.signup_user(user_data)
    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail='User already exist'
        )

    return user


@router.post('/sign-in')
def signin_user(auth_user: GetAuthUser, user_service: GetUserService):
    access_token_expires = timedelta(
        minutes=jwt_env.ACCESS_TOKEN_EXPIRE_MINUTES
    )

    access_token = create_access_token(
        data={'sub': str(auth_user.id)}, expires_delta=access_token_expires
    )

    return CreateToken(access_token=access_token, token_type='bearer')
