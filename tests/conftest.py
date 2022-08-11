from typing import Dict
from uuid import UUID, uuid4

import pytest
from django.test import Client


@pytest.fixture
def client() -> Client:
    return Client()
