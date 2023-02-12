from app.db import SessionLocal
from app.users.exceptions import LanguageExceptionName
from app.users.repository import LanguageRepository


class LanguageService:
    @staticmethod
    def create_language(language_name: str):
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
        try:
            with SessionLocal() as db:
                language_repository = LanguageRepository(db)
                return language_repository.read_all_languages()
        except Exception as e:
            raise e

    @staticmethod
    def read_language_by_id(language_id: str):
        try:
            with SessionLocal() as db:
                language_repository = LanguageRepository(db)
                return language_repository.read_language_by_id(language_id)
        except Exception as e:
            raise e

    @staticmethod
    def read_language_by_name(language_name: str):
        try:
            with SessionLocal() as db:
                language_repository = LanguageRepository(db)
                return language_repository.read_language_by_name(language_name)
        except Exception as e:
            raise e

    @staticmethod
    def delete_language_by_id(language_id: str):
        try:
            with SessionLocal() as db:
                language_repository = LanguageRepository(db)
                return language_repository.delete_language_by_id(language_id)
        except Exception as e:
            raise e
