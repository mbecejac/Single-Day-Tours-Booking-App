from datetime import date
from typing import Optional

from pydantic import UUID4, BaseModel


class TourSchema(BaseModel):
    id: UUID4
    tour_name: str
    date: date
    location: str
    description: str
    price: float
    is_walking_tour: bool
    tour_language: str
    tour_guide_id: str
    bus_carrier_id: str

    class Config:
        orm_mode = True


class TourSchemaInput(BaseModel):
    tour_name: str
    date: date
    location: str
    description: str
    price: float
    is_walking_tour: bool
    tour_language: str
    tour_guide_id: str
    bus_carrier_id: str

    class Config:
        orm_mode = True


class TourSchemaUpdate(BaseModel):
    tour_name: Optional[str]
    date: Optional[date]
    location: Optional[str]
    description: Optional[str]
    price: Optional[float]
    is_walking_tour: Optional[bool]
    tour_language: Optional[str]
    tour_guide_id: Optional[str]
    bus_carrier_id: Optional[str]

    class Config:
        orm_mode = True
