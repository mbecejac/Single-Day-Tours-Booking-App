from uuid import uuid4

from sqlalchemy import Column, ForeignKey, String, UniqueConstraint
from sqlalchemy.orm import relationship

from app.db import Base


class Client(Base):
    __tablename__ = "clients"

    id = Column(String(50), primary_key=True, default=uuid4)
    name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    phone_number = Column(String(30), nullable=False)
    address = Column(String(60))
    city = Column(String(30))

    user_id = Column(String(50), ForeignKey("users.id"), nullable=False)
    user = relationship("User", lazy="subquery")

    __table_args__ = (UniqueConstraint("name", "last_name", "phone_number", name="name_lastname_phone_uc"),)

    def __init__(self, name, last_name, phone_number, address, city, user_id):
        self.name = name
        self.last_name = last_name
        self.phone_number = phone_number
        self.address = address
        self.city = city
        self.user_id = user_id
