"""Language related controllers"""
from fastapi import HTTPException

from app.users.exceptions import LanguageExceptionName, LanguageNotFoundException
from app.users.services import LanguageService


class LanguageController:
    """Controller for language management"""

    @staticmethod
    def create_language(language_name: str):
        """Create a new language"""
        try:
            language = LanguageService.create_language(language_name)
            return language
        except LanguageExceptionName as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            print(e)
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_all_languages():
        """Get all languages"""
        return LanguageService.read_all_languages()

    @staticmethod
    def get_language_by_id(language_id: str):
        """Get languages by provided language id"""
        try:
            language = LanguageService.read_language_by_id(language_id)
            return language
        except LanguageNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_language_by_name(language_name: str):
        """Get languages by provided language name"""
        try:
            language = LanguageService.read_language_by_name(language_name)
            return language
        except LanguageNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def delete_language_by_id(language_id: str):
        """Delete language by provided language id"""
        try:
            LanguageService.delete_language_by_id(language_id)
            return {"message": f"Language with id: {language_id} is deleted"}
        except LanguageNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
