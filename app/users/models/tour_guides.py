"""Tour guide related models"""
from uuid import uuid4

from sqlalchemy import Boolean, Column, ForeignKey, String, UniqueConstraint
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

    language_id = Column(String(50), ForeignKey("languages.id"), nullable=False)
    language = relationship("Language", lazy="subquery")

    is_employee = Column(Boolean, default=False)

    __table_args__ = (
        UniqueConstraint("name", "last_name", "phone_number", "language_id", name="name_lastname_phone_language_uc"),
    )

    def __init__(self, name, last_name, phone_number, user_id, language_id, is_employee=False):
        self.name = name
        self.last_name = last_name
        self.phone_number = phone_number
        self.user_id = user_id
        self.language_id = language_id
        self.is_employee = is_employee
