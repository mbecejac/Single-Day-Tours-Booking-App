"""Employee related models"""
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db import Base


class Employee(Base):
    __tablename__ = "employees"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)

    user_id = Column(String(50), ForeignKey("users.id"))
    user = relationship("User", lazy="joined")

    def __init__(self, user_id):
        self.user_id = user_id
