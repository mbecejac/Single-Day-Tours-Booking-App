"""Language related schemas"""
from pydantic import UUID4, BaseModel


class LanguageSchema(BaseModel):
    id: UUID4
    language_name: str

    class Config:
        orm_mode = True


class LanguageSchemaInput(BaseModel):
    language_name: str

    class Config:
        orm_mode = True
