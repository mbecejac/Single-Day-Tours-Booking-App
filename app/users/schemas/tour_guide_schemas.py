from pydantic import UUID4, BaseModel

from app.users.schemas import LanguageSchema, UserSchema


class TourGuideSchema(BaseModel):
    id: UUID4
    name: str
    last_name: str
    phone_number: str
    user_id: str
    user: UserSchema
    language_id: str
    language: LanguageSchema
    is_employee: bool

    class Config:
        orm_mode = True


class TourGuideSchemaInput(BaseModel):
    name: str
    last_name: str
    phone_number: str
    user_id: str
    language_id: str
    is_employee: bool

    class Config:
        orm_mode = True


# class TourGuideSchemaUpdate(BaseModel):
#     name: Optional[str]
#     last_name: Optional[str]
#     phone_number: Optional[str]
#     user_id: Optional[str]
#     language_id: Optional[str]
#     is_employee: Optional[bool]
#
#     class Config:
#         orm_mode = True
