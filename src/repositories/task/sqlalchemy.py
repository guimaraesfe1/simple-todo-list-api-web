from typing import Any, Optional, Sequence

from sqlalchemy import select
from sqlalchemy.exc import IntegrityError, NoResultFound
from sqlalchemy.orm import Session

from src.models.task import Task
from src.repositories.base import BaseRepository


class TaskSQLAlchemyRepository(BaseRepository[Task]):
    def __init__(self, session: Session):
        self.session = session

    def save(self, entity: Task) -> Task:
        try:
            self.session.add(entity)
            self.session.commit()
        except IntegrityError:
            self.session.rollback()
            raise

        self.session.refresh(entity)

        return entity

    def remove(self, entity: Task) -> None:
        self.session.delete(entity)
        self.session.commit()

    def update(self, entity: Task, entity_data_dict: dict[str, Any]) -> Task:
        for field, value in entity_data_dict.items():
            setattr(entity, field, value)

        try:
            self.session.commit()
        except IntegrityError:
            self.session.rollback()
            raise

        self.session.refresh(entity)

        return entity

    # def exists(self, entity_id: int) -> bool:
    #     stmt = select(Task).where(Task.id == entity_id)

    #     task = self.session.scalars(stmt).one_or_none()

    #     return True if task else False

    # def find_all(self) -> Sequence[Task]:
    #     stmt = select(Task)

    #     list_task = self.session.scalars(stmt).all()

    #     return list_task

    def find_by_id(self, entity_id: int) -> Task:
        stmt = select(Task).where(Task.id == entity_id)

        try:
            task = self.session.scalars(stmt).one()
        except NoResultFound:
            self.session.rollback()
            raise

        return task
