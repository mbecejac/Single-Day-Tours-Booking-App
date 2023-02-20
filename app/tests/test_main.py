from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.config import settings
from app.db import Base
from app.main import app

MYSQL_URL_TEST = f"{settings.DB_HOST}://{settings.DB_USER}:{settings.DB_PASSWORD}@{settings.DB_HOSTNAME}:{settings.DB_PORT}/{settings.DB_NAME_TEST}"

engine = create_engine(MYSQL_URL_TEST, echo=True)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

client = TestClient(app)


class TestClass:
    def setup_method(self, method):
        """Invoked for every test method of a class"""
        Base.metadata.create_all(bind=engine)

    def teardown_method(self, method):
        """Teardown state that was set by a setup_method call"""
        Base.metadata.drop_all(bind=engine)
