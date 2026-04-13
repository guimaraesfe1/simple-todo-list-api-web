from sqlalchemy.exc import IntegrityError, NoResultFound
from sqlalchemy.orm import Session

from src.models.task import Task
from src.repositories.base import BaseRepository
from src.repositories.task.sqlalchemy import TaskSQLAlchemyRepository
from src.schemas.task import CreateUserSchema, UpdateUserSchema


class TaskService:
    def __init__(self, session: Session):
        self.task_repo: BaseRepository = TaskSQLAlchemyRepository(session)

    def create_task(self, task_data: CreateUserSchema, user_id: int):
        task_data_dict = task_data.model_dump()

        new_task = Task(**task_data_dict)

        try:
            return self.task_repo.save(new_task)
        except IntegrityError:
            raise

    def update_task(
        self, task_id: int, task_data: UpdateUserSchema, user_id: int
    ) -> Task | None:
        try:
            task = self.get_task_by_id(task_id, user_id)
        except NoResultFound:
            raise

        task_data_dict = task_data.model_dump(exclude_none=True)

        return self.task_repo.update(task, task_data_dict)

    def get_task_by_id(self, task_id: int, user_id: int) -> Task:
        try:
            task = self.task_repo.find_by_id(task_id)
        except NoResultFound:
            raise

        if task.user_id != user_id:
            raise NoResultFound

        return task

    def delete_task(self, task_id: int, user_id: int):
        try:
            task = self.get_task_by_id(task_id, user_id)
        except NoResultFound:
            raise

        self.task_repo.remove(task)
