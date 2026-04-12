from fastapi import APIRouter, HTTPException, status
from sqlalchemy.exc import IntegrityError, NoResultFound

from src.dependencies.task import GetTaskService
from src.schemas.task import BaseTaskSchema, CreateUserSchema, UpdateUserSchema

router = APIRouter(prefix='/task', tags=['Task CRUD'])


@router.post(
    '', status_code=status.HTTP_201_CREATED, response_model=BaseTaskSchema
)
def create_task(task_data: CreateUserSchema, task_service: GetTaskService):

    try:
        task = task_service.create_task(task_data)
    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail='Task not unique'
        )

    return task


@router.get(
    '/{task_id}', status_code=status.HTTP_200_OK, response_model=BaseTaskSchema
)
def get_task_by_id(task_id: int, task_service: GetTaskService):

    try:
        task = task_service.get_task_by_id(task_id)
    except NoResultFound:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='Task not found'
        )

    return task


@router.delete('/{task_id}', status_code=status.HTTP_200_OK)
def delete_task(task_id: int, task_service: GetTaskService):
    try:
        task_service.delete_task(task_id)
    except NoResultFound:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='Task Not found'
        )

    return {'message': 'Task removed succesfully'}


@router.put(
    '/{task_id}', status_code=status.HTTP_200_OK, response_model=BaseTaskSchema
)
def update_task(
    task_id: int, task_data: UpdateUserSchema, task_service: GetTaskService
):
    try:
        task = task_service.update_task(task_id, task_data)
    except NoResultFound:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='Task Not found'
        )

    return task
