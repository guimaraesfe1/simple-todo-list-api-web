from datetime import datetime, timedelta, timezone
from src.utils.jwt_env import jwt_env

import jwt


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()

    expire = (
        datetime.now(timezone.utc) + expires_delta
        if expires_delta
        else timedelta(minutes=15)
    )

    to_encode.update({'exp': expire})

    encoded_jwt = jwt.encode(
        to_encode, jwt_env.SECRET_KEY, algorithm=jwt_env.ALGORITHM
    )

    return encoded_jwt
