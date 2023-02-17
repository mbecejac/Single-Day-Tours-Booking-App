from uuid import uuid4

from sqlalchemy import Boolean, Column, ForeignKey, String
from sqlalchemy.orm import relationship

from app.db import Base


class TourApplication(Base):
    __tablename__ = "tour_applications"
    id = Column(String(50), primary_key=True, default=uuid4)
    is_payed = Column(Boolean, default=False)

    client_id = Column(String(50), ForeignKey("clients.id"), nullable=False)
    client = relationship("Client", lazy="subquery")

    tour_id = Column(String(50), ForeignKey("tours.id"), nullable=False)
    tour = relationship("Tour", lazy="subquery")

    def __init__(self, is_payed, client_id, tour_id):
        self.is_payed = is_payed
        self.client_id = client_id
        self.tour_id = tour_id
