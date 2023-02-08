from sqlalchemy import Column, String, Boolean
from uuid import uuid4
from app.db import Base


class User(Base):
    __tablename__ = "users"
    id = Column(String(50), primary_key=True, default=uuid4)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    is_active = Column(Boolean)
    is_superuser = Column(Boolean, default=False)

    def __init__(self, email, password, is_active=True, is_superuser=False):
        self.email = email
        self.password = password
        self.is_active = is_active
        self.is_superuser = is_superuser
