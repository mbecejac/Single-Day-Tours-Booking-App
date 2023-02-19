from datetime import date

from pydantic import UUID4, BaseModel


class TourSchema(BaseModel):
    id: UUID4
    tour_name: str
    tour_date: date
    location: str
    description: str
    price: float
    is_walking_tour: bool
    tour_language: str
    tour_guide_id: str
    bus_carrier_id: str
    is_active: bool

    class Config:
        orm_mode = True


class TourSchemaInput(BaseModel):
    tour_name: str
    tour_date: str
    location: str
    description: str
    price: float
    is_walking_tour: bool
    tour_language: str
    tour_guide_id: str

    class Config:
        orm_mode = True
