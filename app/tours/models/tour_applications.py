from uuid import uuid4

from sqlalchemy import Boolean, Column, ForeignKey, String, UniqueConstraint
from sqlalchemy.orm import relationship

from app.db import Base


class TourApplication(Base):
    __tablename__ = "tour_applications"
    id = Column(String(50), primary_key=True, default=uuid4)

    customer_id = Column(String(50), ForeignKey("customers.id"), nullable=False)
    customer = relationship("Customer", lazy="subquery")

    tour_id = Column(String(50), ForeignKey("tours.id"), nullable=False)
    tour = relationship("Tour", lazy="subquery")

    is_payed = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)

    __table_args__ = (UniqueConstraint("customer_id", "tour_id", name="customer_tour_uc"),)

    def __init__(self, customer_id, tour_id, is_payed=False, is_active=True):
        self.customer_id = customer_id
        self.tour_id = tour_id
        self.is_payed = is_payed
        self.is_active = is_active
