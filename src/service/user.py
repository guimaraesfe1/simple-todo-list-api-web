from sqlalchemy.exc import IntegrityError, NoResultFound
from sqlalchemy.orm import Session

from src.models.user import User
from src.repositories.user.sqlalchemy import UserSQLAlchemyRepository
from src.schemas.user import SignUpUserSchema
from src.utils.hash import get_passwd_hash, verify_password


class InvalidCredentials(Exception):
    pass


class UserService:
    def __init__(self, session: Session):
        self.user_repo = UserSQLAlchemyRepository(session)

    def signup_user(self, user_data: SignUpUserSchema):
        user_data.password = get_passwd_hash(user_data.password)

        user_data_dict = user_data.model_dump()

        new_user = User(**user_data_dict)

        try:
            return self.user_repo.save(new_user)
        except IntegrityError:
            raise

    def get_user_by_email(self, email):
        try:
            user = self.user_repo.find_by_label(email)
        except NoResultFound:
            raise

        return user

    def get_user_by_id(self, user_id: int) -> User:
        return self.user_repo.find_by_id(user_id)
