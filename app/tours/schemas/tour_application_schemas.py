from pydantic import UUID4, BaseModel

from app.tours.schemas.tour_schemas import TourSchema
from app.users.schemas.customer_schemas import CustomerSchema


class TourApplicationSchema(BaseModel):
    id: UUID4
    customer_id: str
    customer: CustomerSchema
    tour_id: str
    tour: TourSchema
    is_payed: bool
    is_active: bool

    class Config:
        orm_mode = True


class TourApplicationSchemaInput(BaseModel):
    customer_id: str
    tour_id: str

    class Config:
        orm_mode = True
