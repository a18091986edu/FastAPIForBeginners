from fastapi import APIRouter, Depends
from typing import Annotated

from sqlalchemy import Select

from schemas.task import STask, STaskAdd
from models.tasks import TaskModel

from database import SessionDep

router = APIRouter(prefix="/tasks", tags=["Задачи"])


@router.post("", response_model=STask)
async def create_task(task: STaskAdd, session: SessionDep):
    new_task = TaskModel(**task.model_dump())  # распаковка словаря
    session.add(new_task)
    await session.commit()
    await session.refresh(new_task)
    return new_task


@router.get("")
async def get_tasks(session: SessionDep):
    query = Select(TaskModel)
    result = await session.execute(query)
    tasks = result.scalars().all()
    return tasks
