from typing import Annotated

from fastapi import Depends

from src.service.task import TaskService

from .session import GetSession


def get_task_service(session: GetSession):
    return TaskService(session)


GetTaskService = Annotated[TaskService, Depends(get_task_service)]
