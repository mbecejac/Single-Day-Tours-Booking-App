"""Language related repositories"""
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.users.exceptions import LanguageNotFoundException
from app.users.models.languages import Language


class LanguageRepository:
    """Repository for Language management."""

    def __init__(self, db: Session):
        """
        Initialize the LanguageRepository database connection.

        :param db: Session instance for database connection
        :type db: Session
        """
        self.db = db

    def create_language(self, language_name: str):
        """Create language."""
        try:
            language = Language(language_name)
            self.db.add(language)
            self.db.commit()
            self.db.refresh(language)
            return language
        except IntegrityError as e:
            raise e
        except Exception as e:
            raise e

    def read_all_languages(self):
        """Read all languages"""
        return self.db.query(Language).all()

    def read_language_by_id(self, language_id: str):
        """Read language by provided id"""
        language = self.db.query(Language).filter(Language.id == language_id).first()
        if language is None:
            raise LanguageNotFoundException(message=f"Language with provided id: {language_id} not found", code=400)
        return language

    def read_language_by_name(self, language_name: str):
        """Read language by provided name"""
        language = self.db.query(Language).filter(Language.language_name == language_name).first()
        return language

    def delete_language_by_id(self, language_id: str):
        """Delete language by provided id"""
        try:
            language = self.db.query(Language).filter(Language.id == language_id).first()
            if language is None:
                raise LanguageNotFoundException(message=f"Language with provided id: {language_id} not found", code=400)
            self.db.delete(language)
            self.db.commit()
            return True
        except Exception as e:
            raise e
