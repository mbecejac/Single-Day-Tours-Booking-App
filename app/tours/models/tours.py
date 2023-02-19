from datetime import datetime
from uuid import uuid4

from sqlalchemy import Boolean, Column, Date, Float, ForeignKey, String
from sqlalchemy.orm import relationship

from app.db import Base


class Tour(Base):
    __tablename__ = "tours"
    id = Column(String(50), primary_key=True, default=uuid4)
    tour_name = Column(String(50), nullable=False)
    tour_date = Column(Date, nullable=False)
    location = Column(String(50), nullable=False)
    description = Column(String(300))
    price = Column(Float, nullable=False)
    is_walking_tour = Column(Boolean, default=False)
    tour_language = Column(String(50))

    tour_guide_id = Column(String(50), ForeignKey("tour_guides.id"), nullable=False)
    tour_guide = relationship("TourGuide", lazy="subquery")

    bus_carrier_id = Column(String(50), ForeignKey("bus_carriers.id"), nullable=False)

    is_active = Column(Boolean, default=True)

    def __init__(
        self,
        tour_name: str,
        tour_date: str,
        location: str,
        description: str,
        price: float,
        is_walking_tour: bool,
        tour_language: str,
        tour_guide_id: str,
        bus_carrier_id: str,
        is_active: bool = True,
    ):
        self.tour_name = tour_name
        self.tour_date = datetime.strptime(tour_date, "%d-%m-%Y")
        self.location = location
        self.description = description
        self.price = price
        self.is_walking_tour = is_walking_tour
        self.tour_language = tour_language
        self.tour_guide_id = tour_guide_id
        self.bus_carrier_id = bus_carrier_id
        self.is_active = is_active
