"""Language related services"""
from app.db import SessionLocal
from app.users.exceptions import LanguageExceptionName
from app.users.repositories import LanguageRepository


class LanguageService:
    """Service for language management"""

    @staticmethod
    def create_language(language_name: str):
        """Create a new language."""
        try:
            with SessionLocal() as db:
                language_repository = LanguageRepository(db)
                language_check = language_repository.read_language_by_name(language_name)
                if language_check is None:
                    return language_repository.create_language(language_name)
                raise LanguageExceptionName(message="Language already exists.", code=400)
        except Exception as e:
            print(e)
            raise e

    @staticmethod
    def read_all_languages():
        """Read all languages."""
        try:
            with SessionLocal() as db:
                language_repository = LanguageRepository(db)
                return language_repository.read_all_languages()
        except Exception as e:
            raise e

    @staticmethod
    def read_language_by_id(language_id: str):
        """Read language by provided id."""
        try:
            with SessionLocal() as db:
                language_repository = LanguageRepository(db)
                return language_repository.read_language_by_id(language_id)
        except Exception as e:
            raise e

    @staticmethod
    def read_language_by_name(language_name: str):
        """Read language by provided name."""
        try:
            with SessionLocal() as db:
                language_repository = LanguageRepository(db)
                return language_repository.read_language_by_name(language_name)
        except Exception as e:
            raise e

    @staticmethod
    def delete_language_by_id(language_id: str):
        """Delete language by provided id."""
        try:
            with SessionLocal() as db:
                language_repository = LanguageRepository(db)
                return language_repository.delete_language_by_id(language_id)
        except Exception as e:
            raise e
