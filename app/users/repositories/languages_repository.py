from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.users.exceptions import LanguageNotFoundException
from app.users.models.languages import Language


class LanguageRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_language(self, language_name: str):
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
        return self.db.query(Language).all()

    def read_language_by_id(self, language_id: str):
        language = self.db.query(Language).filter(Language.id == language_id).first()
        if language is None:
            raise LanguageNotFoundException(message=f"Language with provided id: {language_id} not found", code=400)
        return language

    def read_language_by_name(self, language_name: str):
        language = self.db.query(Language).filter(Language.language_name == language_name).first()
        return language

    def delete_language_by_id(self, language_id: str):
        try:
            language = self.db.query(Language).filter(Language.id == language_id).first()
            if language is None:
                raise LanguageNotFoundException(message=f"Language with provided id: {language_id} not found", code=400)
            self.db.delete(language)
            self.db.commit()
            return True
        except Exception as e:
            raise e
