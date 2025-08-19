import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.db.session import engine, SessionLocal
from app.db.base import Base


@pytest.fixture(autouse=True, scope="session")
def create_db():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


@pytest.fixture()
def client():
    return TestClient(app)
