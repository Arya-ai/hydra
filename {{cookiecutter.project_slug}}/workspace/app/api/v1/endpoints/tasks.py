from celery import group
from fastapi import APIRouter, Depends

from app.api.utils.security import get_current_active_user
from app.models.user import User as DBUser
from app.schemas.task import (Task, TaskChain, TaskNoResult, TaskNoResultGroup,
                              TaskResult, TaskResultGroup)
from app.tasks.task import (celery_sleep_task_no_result,
                            celery_sleep_task_with_result)

router = APIRouter()

@router.post("/celery-task-no-result", response_model=TaskNoResult)
def celery_task_no_result(
    *,
    task_in: Task,
    current_user: DBUser = Depends(get_current_active_user)
):
    task = celery_sleep_task_no_result.delay(task_in.number)
    return TaskNoResult(id=task_in.id, status=task.status)


@router.post("/celery-task-group-no-result", response_model=TaskNoResultGroup)
def celery_task_no_result_group(
    *,
    task_in: TaskChain,
    current_user: DBUser = Depends(get_current_active_user)
):
    group_signature = group(celery_sleep_task_no_result.s(number) for number in task_in.numbers)
    group_result = group_signature.delay()
    individual_results = group_result.children
    return TaskNoResultGroup(id=task_in.id, status=[result.status for result in individual_results])


@router.post("/celery-task-result", response_model=TaskResult)
def celery_task_result(
    *,
    task_in: Task,
    current_user: DBUser = Depends(get_current_active_user)
):
    task = celery_sleep_task_with_result.delay(task_in.number)
    
    # Blocking call
    result = task.get()
    return TaskResult(id=task_in.id, status=task.status, result=result)


@router.post("/celery-task-group-result", response_model=TaskResultGroup)
def celery_task_result_group(
    *,
    task_in: TaskChain,
    current_user: DBUser = Depends(get_current_active_user)
):
    group_signature = group(celery_sleep_task_with_result.s(number) for number in task_in.numbers)
    group_result = group_signature.delay()

    # Blocking call
    results = group_result.get()
    status = [subtask.status for subtask in group_result.children]
    return TaskResultGroup(id=task_in.id, status=status, results=results)
