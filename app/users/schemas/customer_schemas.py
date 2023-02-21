from typing import Optional

from pydantic import UUID4, BaseModel

from app.users.schemas import UserSchema


class CustomerSchema(BaseModel):
    id: UUID4
    name: str
    last_name: str
    phone_number: str
    address: str
    city: str
    user_id: str
    user: UserSchema

    class Config:
        orm_mode = True


class CustomerSchemaInput(BaseModel):
    name: str
    last_name: str
    phone_number: str
    address: str
    city: str
    user_id: str

    class Config:
        orm_mode = True


class CustomerSchemaUpdate(BaseModel):
    id: Optional[str]
    name: Optional[str]
    last_name: Optional[str]
    phone_number: Optional[str]
    address: Optional[str]
    city: Optional[str]

    class Config:
        orm_mode = True
