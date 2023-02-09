from uuid import uuid4

from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db import Base


class TourGuide(Base):
    __tablename__ = "tour_guides"
    id = Column(String(50), primary_key=True, default=uuid4)
    name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    phone_number = Column(String(30), nullable=False)

    user_id = Column(String(50), ForeignKey("users.id"), nullable=False)
    user = relationship("User", lazy="subquery")

    employee_id = Column(String(50), ForeignKey("employees.id"))

    language_id = Column(String(50), ForeignKey("languages.id"))

    def __init__(self, name, last_name, phone_number, user_id, employee_id, language_id):
        self.name = name
        self.last_name = last_name
        self.phone_number = phone_number
        self.user_id = user_id
        self.employee_id = employee_id
        self.language_id = language_id
