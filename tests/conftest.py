from typing import Dict
from uuid import UUID, uuid4

import pytest
from django.test import Client


@pytest.fixture
def fake_user() -> UUID:
    return uuid4()


@pytest.fixture
def fake_payload(fake_user: UUID) -> Dict:
    return {"id": fake_user}


@pytest.fixture
def client() -> Client:
    return Client()
