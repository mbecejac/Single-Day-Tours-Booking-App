from typing import Optional

from pydantic import UUID4, BaseModel

from app.users.schemas import UserSchema


class TourGuideSchema(BaseModel):
    id: UUID4
    name: str
    last_name: str
    phone_number: str
    user_id: str
    user: UserSchema
    employee_id: str
    language_id: str

    class Config:
        orm_mode = True


class TourGuideSchemaInput(BaseModel):
    name: str
    last_name: str
    phone_number: str
    user_id: str
    employee_id: str
    language_id: str

    class Config:
        orm_mode = True


class TourGuideSchemaUpdate(BaseModel):
    name: Optional[str]
    last_name: Optional[str]
    phone_number: Optional[str]
    user_id: Optional[str]
    employee_id: Optional[str]
    language_id: Optional[str]

    class Config:
        orm_mode = True
