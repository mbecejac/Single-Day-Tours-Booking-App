from datetime import datetime
from uuid import uuid4

from sqlalchemy import Column, String, Date, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from app.db import Base


class Tour(Base):
    __tablename__ = "tours"
    id = Column(String(50), primary_key=True, default=uuid4)
    tour_name = Column(String(50), nullable=False)
    date = Column(Date, nullable=False)
    location = Column(String(50), nullable=False)
    description = Column(String(300))
    price = Column(Float, nullable=False)
    is_walking_tour = Column(Boolean, default=False)
    tour_language = Column(String(30), default="Serbian")

    tour_guide_id = Column(String(50), ForeignKey("tour_guides.id"), nullable=False)
    tour_guide = relationship("TourGuide", lazy="subquery")

    bus_carrier_id = Column(String(50), ForeignKey("bus_carriers.id"), nullable=False)

    def __init__(
        self,
        tour_name: str,
        date: str,
        location: str,
        description: str,
        price: float,
        is_walking_tour: bool,
        tour_language: str,
        tour_guide_id: str,
        bus_carrier_id: str,
    ):
        self.tour_name = tour_name
        self.date = datetime.strptime(date, "%d-%m-%Y")
        self.location = location
        self.description = description
        self.price = price
        self.is_walking_tour = is_walking_tour
        self.tour_language = tour_language
        self.tour_guide_id = tour_guide_id
        self.bus_carrier_id = bus_carrier_id
