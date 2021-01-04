from typing import Dict

from fastapi.testclient import TestClient

from app.core import config


def test_celery_task_no_result(
    client: TestClient,
    superuser_token_headers: Dict[str, str]
) -> None:
    data = {"id": "TEST_NO_RESULT", "number": 1}
    r = client.post(
        f"{config.API_V1_STR}/tasks/celery-task-no-result",
        json=data,
        headers=superuser_token_headers
    )
    response = r.json()
    assert r.status_code == 200
    assert response["status"]


def test_celery_task_no_result_group(
    client: TestClient,
    superuser_token_headers: Dict[str, str]
) -> None:
    data = {"id": "TEST_NO_RESULT_GROUP", "numbers": [1,2]}
    r = client.post(
        f"{config.API_V1_STR}/tasks/celery-task-group-no-result",
        json=data,
        headers=superuser_token_headers
    )
    response = r.json()
    assert r.status_code == 200
    assert response["status"]


def test_celery_task_result(
    client: TestClient,
    superuser_token_headers: Dict[str, str]
) -> None:
    data = {"id": "TEST_RESULT", "number": 1}
    r = client.post(
        f"{config.API_V1_STR}/tasks/celery-task-result",
        json=data,
        headers=superuser_token_headers
    )
    response = r.json()
    assert r.status_code == 200
    assert response["status"]
    assert response["result"] == 1


def test_celery_task_result_group(
    client: TestClient,
    superuser_token_headers: Dict[str, str]
) -> None:
    data = {"id": "TEST_RESULT_GROUP", "numbers": [1,2]}
    r = client.post(
        f"{config.API_V1_STR}/tasks/celery-task-group-result",
        json=data,
        headers=superuser_token_headers
    )
    response = r.json()
    assert r.status_code == 200
    assert response["status"]
    assert response["results"] == [1,4]
