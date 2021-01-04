from typing import Dict

from fastapi.testclient import TestClient

from app.core import config


def test_get_access_token(client: TestClient) -> None:
    login_data = {
        "username": config.SUPERUSER_EMAIL,
        "password": config.SUPERUSER_PASSWORD,
    }
    r = client.post(f"{config.API_V1_STR}/login/access-token", data=login_data)
    tokens = r.json()
    assert r.status_code == 200
    assert "access_token" in tokens
    assert tokens["access_token"]


def test_use_access_token(
    client: TestClient, superuser_token_headers: Dict[str, str]
) -> None:
    r = client.post(
        f"{config.API_V1_STR}/login/test-token", headers=superuser_token_headers,
    )
    result = r.json()
    assert r.status_code == 200
    assert "email" in result
