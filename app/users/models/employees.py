from uuid import uuid4

from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db import Base


class Employee(Base):
    __tablename__ = "employees"
    id = Column(String(50), primary_key=True, default=uuid4)

    user_id = Column(String(50), ForeignKey("users.id"), nullable=False)
    user = relationship("User", lazy="subquery")

    def __init__(self, user_id):
        self.user_id = user_id
