from typing import Optional

from pydantic import UUID4, BaseModel

from app.tours.schemas.tour_schemas import TourSchema
from app.users.schemas.customer_schemas import ClientSchema


class TourApplicationSchema(BaseModel):
    id: UUID4
    is_payed: bool
    client_id: str
    client: ClientSchema
    tour_id: str
    tour: TourSchema

    class Config:
        orm_mode = True


class TourApplicationSchemaInput(BaseModel):
    is_payed: bool
    client_id: str
    tour_id: str

    class Config:
        orm_mode = True


class TourApplicationSchemaUpdate(BaseModel):
    is_payed: Optional[bool]
    client_id: Optional[str]
    tour_id: Optional[str]

    class Config:
        orm_mode = True
