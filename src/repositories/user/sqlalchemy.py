from typing import Any

from sqlalchemy import select
from sqlalchemy.exc import IntegrityError, NoResultFound
from sqlalchemy.orm import Session

from src.models.user import User
from src.repositories.base import BaseRepository


class UserSQLAlchemyRepository(BaseRepository[User]):
    def __init__(self, session: Session):
        self.session = session

    def save(self, entity: User) -> User:
        self.session.add(entity)
        try:
            self.session.commit()
            self.session.refresh(entity)
        except IntegrityError:
            self.session.rollback()
            raise

        return entity

    def remove(self, entity: User) -> None:
        self.session.delete(entity)
        self.session.commit()

    def update(self, entity: User, entity_data_dict: dict[str, Any]) -> User:
        for field, value in entity_data_dict.items():
            setattr(entity, field, value)

        try:
            self.session.commit()
        except IntegrityError:
            self.session.rollback()
            raise

        self.session.refresh(entity)

        return entity

    def find_by_id(self, entity_id: int) -> User:
        stmt = select(User).where(User.id == entity_id)

        try:
            user = self.session.scalars(stmt).one()
        except NoResultFound:
            self.session.rollback()
            raise

        return user

    def find_by_label(self, entity_label: str) -> User:
        stmt = select(User).where(User.email == entity_label)

        try:
            user = self.session.scalars(stmt).one()
        except NoResultFound:
            self.session.rollback()
            raise

        return user
