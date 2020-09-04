from typing import List

from pydantic import BaseModel
from pydantic import EmailStr, HttpUrl


# Shared Properties
class TaskBase(BaseModel):
    id: str


# Properties to receive for a task via API
class Task(TaskBase):
    number: int


# Properties to receive for a task chain via API
class TaskChain(TaskBase):
    numbers: List[int]


# Properties to send for task with no result via API
class TaskNoResult(TaskBase):
    status: str


# Properties to send for task with no result group via API
class TaskNoResultGroup(TaskBase):
    status: List[str]


# Properties to send for task with result via API
class TaskResult(TaskNoResult):
    result: int


# Properties to send for task with result group via API
class TaskResultGroup(TaskNoResultGroup):
    results: List[int]
