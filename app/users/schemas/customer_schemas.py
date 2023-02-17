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
