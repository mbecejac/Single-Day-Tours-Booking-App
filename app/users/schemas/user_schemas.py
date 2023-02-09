from pydantic import UUID4, BaseModel, EmailStr


class UserSchema(BaseModel):
    id: UUID4
    email: EmailStr
    password: str
    is_active: bool
    is_superuser: bool

    class Config:
        orm_mode = True


class UserSchemaInput(BaseModel):
    email: EmailStr
    password: str

    class Config:
        orm_mode = True
