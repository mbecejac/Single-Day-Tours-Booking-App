from typing import Optional

from pydantic import BaseModel, UUID4, EmailStr


class BusCarrierSchema(BaseModel):
    id: UUID4
    name: str
    email: EmailStr
    phone_number: str
    address: str
    city: str

    class Config:
        orm_mode = True


class BusCarrierSchemaInput(BaseModel):
    name: str
    email: EmailStr
    phone_number: str
    address: str
    city: str

    class Config:
        orm_mode = True


class BusCarrierSchemaUpdate(BaseModel):
    name: Optional[str]
    email: Optional[EmailStr]
    phone_number: Optional[str]
    address: Optional[str]
    city: Optional[str]

    class Config:
        orm_mode = True





