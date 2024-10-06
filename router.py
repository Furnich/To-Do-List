from typing import Annotated
from fastapi import APIRouter, Depends
from repository import TaksRepository
from schemas import STask, STaskAdd, STaskId

router = APIRouter(
    prefix='/tasks',
    tags=['Таски'],
)

@router.post("")
async def add_task(
    task: Annotated[STaskAdd, Depends()],
) -> STaskId:
    task_id = await TaksRepository.add_one(task)
    return {"ok":True, 'task_id': task_id}



@router.get("")
async def get_tasks() -> list[STask]:
    try:
        tasks = await TaksRepository.find_all()
        return tasks
    except Exception as e:
        print(f"Ошибка при получении задач: {e}")  # Вывод ошибки
        return []

