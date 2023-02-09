from typing import Optional

from pydantic import UUID4, BaseModel

from app.users.schemas import UserSchema


class ClientSchema(BaseModel):
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


class ClientSchemaIn(BaseModel):
    name: str
    last_name: str
    phone_number: str
    address: str
    city: str
    user_id: str

    class Config:
        orm_mode = True


class ClientSchemaUpdate(BaseModel):
    name: Optional[str]
    last_name: Optional[str]
    phone_number: Optional[str]
    address: Optional[str]
    city: Optional[str]
    user_id: Optional[str]

    class Config:
        orm_mode = True
