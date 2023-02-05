from uuid import uuid4

from sqlalchemy import Column, String

from app.db import Base


class BusCarrier(Base):
    __tablename__ = "bus_carriers"
    id = Column(String(50), primary_key=True, default=uuid4)
    name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    phone_number = Column(String(30), nullable=False)
    address = Column(String(60))
    city = Column(String(30))

    def __init__(self, name, email, phone_number, address, city):
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.address = address
        self.city = city
