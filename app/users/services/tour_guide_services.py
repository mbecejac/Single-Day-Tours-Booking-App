from app.db import SessionLocal
from app.users.exceptions import LanguageNotFoundException
from app.users.repositories import EmployeeRepository, LanguageRepository, TourGuideRepository


class TourGuideService:
    @staticmethod
    def create_tour_guide(name: str, last_name: str, phone_number: str, user_id: str, language_id: str):
        try:
            with SessionLocal() as db:
                tour_guide_repository = TourGuideRepository(db)
                return tour_guide_repository.create_tour_guide(name, last_name, phone_number, user_id, language_id)
        except Exception as e:
            raise e

    @staticmethod
    def read_all_tour_guides():
        try:
            with SessionLocal() as db:
                tour_guide_repository = TourGuideRepository(db)
                return tour_guide_repository.read_all_tour_guides()
        except Exception as e:
            raise e

    @staticmethod
    def read_tour_guide_by_id(tour_guide_id: str):
        try:
            with SessionLocal() as db:
                tour_guide_repository = TourGuideRepository(db)
                return tour_guide_repository.read_tour_guide_by_id(tour_guide_id)
        except Exception as e:
            raise e

    @staticmethod
    def read_tour_guide_by_user_id(user_id: str):
        try:
            with SessionLocal() as db:
                tour_guide_repository = TourGuideRepository(db)
                return tour_guide_repository.read_tour_guide_by_user_id(user_id)
        except Exception as e:
            raise e

    @staticmethod
    def read_tour_guide_by_name_or_last_name(name_lastname: str):
        try:
            with SessionLocal() as db:
                tour_guide_repository = TourGuideRepository(db)
                return tour_guide_repository.read_tour_guide_by_name_or_lastname(name_lastname)
        except Exception as e:
            raise e

    @staticmethod
    def update_tour_guide_data(tour_guide_id: str, name: str = None, last_name: str = None, phone_number: str = None):
        try:
            with SessionLocal() as db:
                tour_guide_repository = TourGuideRepository(db)
                return tour_guide_repository.update_tour_guide_data(tour_guide_id, name, last_name, phone_number)
        except Exception as e:
            raise e

    @staticmethod
    def update_tour_guide_language(tour_guide_id: str, language_id: str):
        try:
            with SessionLocal() as db:
                tour_guide_repository = TourGuideRepository(db)
                language_repository = LanguageRepository(db)
                language_check = language_repository.read_language_by_id(language_id)
                if language_id == language_check.id:
                    return tour_guide_repository.update_tour_guide_language_id(tour_guide_id, language_id)
                else:
                    raise LanguageNotFoundException(message="Language not found", code=404)
        except Exception as e:
            raise e

    @staticmethod
    def update_tour_guide_is_employee(tour_guide_id: str):
        try:
            with SessionLocal() as db:
                tour_guide_repository = TourGuideRepository(db)
                employee_repository = EmployeeRepository(db)
                tour_guide = tour_guide_repository.read_tour_guide_by_id(tour_guide_id)
                check_is_employee = employee_repository.read_employee_by_user_id(tour_guide.user.id)
                if check_is_employee:
                    return tour_guide_repository.update_tour_guide_is_employee(tour_guide_id)
        except Exception as e:
            raise e

    @staticmethod
    def delete_tour_guide_by_id(tour_guide_id: str):
        try:
            with SessionLocal() as db:
                tour_guide_repository = TourGuideRepository(db)
                return tour_guide_repository.delete_tour_guide_by_id(tour_guide_id)
        except Exception as e:
            raise e
