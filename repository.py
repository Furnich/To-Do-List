
from sqlalchemy import select
from DataBase import TasksOrm, new_session
from schemas import STask, STaskAdd

class TaksRepository:
    @classmethod
    async def add_one(cls, data: STaskAdd) -> int:
        async with new_session() as session:
            task_dict = data.model_dump()

            task = TasksOrm(**task_dict)
            session.add(task)
            await session.flush()
            await session.commit()
            print(f"Добавлена задача: {task_dict}")  # Вывод в консоль
            return task.id



    @classmethod
    async def find_all(cls) -> list[STask]:
        async with new_session() as session:
            result = await session.execute(select(TasksOrm))
            tasks = result.scalars().all()
            print(f"Найденные задачи: {tasks}")  # Вывод в консоль
            return [STask.model_validate(task) for task in tasks]
