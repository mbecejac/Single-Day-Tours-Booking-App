from uuid import uuid4

from sqlalchemy import Column, String

from app.db import Base


class Language(Base):
    __tablename__ = "languages"
    id = Column(String(50), primary_key=True, default=uuid4)
    language_name = Column(String(50))

    def __init__(self, language_name: str):
        self.language_name = language_name
