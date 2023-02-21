from datetime import date
from typing import Optional

from pydantic import UUID4, BaseModel

from app.tours.schemas import BusCarrierSchema
from app.users.schemas import LanguageSchema, TourGuideSchema


class TourSchema(BaseModel):
    id: UUID4
    tour_name: str
    tour_date: date
    location: str
    description: str
    price: float
    is_walking_tour: bool
    tour_language: str
    language: LanguageSchema
    tour_guide_id: str
    tour_guide: TourGuideSchema
    bus_carrier_id: str
    bus_carrier: BusCarrierSchema
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


class TourSchemaPreview(BaseModel):
    id: UUID4
    tour_name: str
    tour_date: date
    location: str
    description: str
    price: float
    is_walking_tour: bool
    tour_language: str
    language: LanguageSchema
    is_active: bool

    class Config:
        orm_mode = True


class TourSchemaTourGuideUpdate(BaseModel):
    id: Optional[str]
    tour_guide_id: Optional[str]


class TourSchemaBusCarrierUpdate(BaseModel):
    id: Optional[str]
    bus_carrier_id: Optional[str]


class TourSchemaIsActiveUpdate(BaseModel):
    id: Optional[str]
    is_active: Optional[bool]
