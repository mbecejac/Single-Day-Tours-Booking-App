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
    tour_guide = relationship("TourGuide", lazy='subquery')

    bus_carrier_id = Column(String(50), ForeignKey("bus_carriers.id"), nullable=False)

