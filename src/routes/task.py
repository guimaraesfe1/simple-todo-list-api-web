from fastapi import APIRouter


router = APIRouter(prefix="/task")


@router.post("")
def create_task():
    pass


@router.get("/{task_id}")
def get_task_by_id(task_id: int):
    pass


@router.delete("/{task_id}")
def delete_task(task_id: int):
    pass


@router.put("/{task_id}")
def update_task(task_id: int):
    pass
