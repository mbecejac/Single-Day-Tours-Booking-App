from pydantic import BaseModel, UUID4

from app.users.schemas import UserSchema


class EmployeeSchema(BaseModel):
    id: UUID4
    user_id: str
    user: UserSchema

    class Config:
        orm_mode = True


class EmployeeSchemaInput(BaseModel):
    user_id: str

    class Config:
        orm_mode = True
