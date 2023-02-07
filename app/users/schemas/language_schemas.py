from pydantic import BaseModel, UUID4


class LanguageSchema(BaseModel):
    id: UUID4
    language_name: str

    class Config:
        orm_mode = True


class LanguageSchemaInput(BaseModel):
    language_name: str

    class Config:
        orm_mode = True

