from fastapi import FastAPI
from contextlib import asynccontextmanager
from DataBase import create_tables, delete_tables
from router import router as tasks_router



@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print('База очищена')
    await create_tables()
    print('База готова')
    yield
    print('Перезагрузка')


app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)
