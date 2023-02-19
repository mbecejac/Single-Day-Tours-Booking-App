from app.db import SessionLocal
from app.tours.exceptions import TourNotFoundException
from app.tours.repositories import TourApplicationRepository, TourRepository
from app.users.exceptions import CustomerNotFoundException
from app.users.repositories import CustomerRepository


class TourApplicationService:
    @staticmethod
    def create_tour_application(customer_id: str, tour_id: str):
        try:
            with SessionLocal() as db:
                tour_application_repository = TourApplicationRepository(db)
                tour_repository = TourRepository(db)
                customer_repository = CustomerRepository(db)
                tour_check = tour_repository.read_tour_by_id(tour_id)
                customer_check = customer_repository.read_customer_by_id(customer_id)
                if tour_check.id == tour_id and customer_check.id == customer_id:
                    return tour_application_repository.create_tour_application(customer_id, tour_id)
        except TourNotFoundException as e:
            raise e
        except CustomerNotFoundException as e:
            raise e
        except Exception as e:
            raise e

    @staticmethod
    def read_all_tour_applications():
        try:
            with SessionLocal() as db:
                tour_application_repository = TourApplicationRepository(db)
                return tour_application_repository.read_all_tour_applications()
        except Exception as e:
            raise e

    @staticmethod
    def read_tour_application_by_id(tour_app_id: str):
        try:
            with SessionLocal() as db:
                tour_application_repository = TourApplicationRepository(db)
                return tour_application_repository.read_tour_application_by_id(tour_app_id)
        except Exception as e:
            raise e

    @staticmethod
    def read_all_active_tour_applications():
        try:
            with SessionLocal() as db:
                tour_application_repository = TourApplicationRepository(db)
                return tour_application_repository.read_all_active_tour_applications()
        except Exception as e:
            raise e

    @staticmethod
    def read_tour_applications_by_customer_id(customer_id: str):
        try:
            with SessionLocal() as db:
                tour_application_repository = TourApplicationRepository(db)
                return tour_application_repository.read_all_tour_applications_by_customer_id(customer_id)
        except Exception as e:
            raise e

    @staticmethod
    def read_tour_applications_by_tour_id(tour_id: str):
        try:
            with SessionLocal() as db:
                tour_application_repository = TourApplicationRepository(db)
                return tour_application_repository.read_all_tour_applications_by_tour_id(tour_id)
        except Exception as e:
            raise e

    @staticmethod
    def read_not_payed_active_tour_applications():
        try:
            with SessionLocal() as db:
                tour_application_repository = TourApplicationRepository(db)
                return tour_application_repository.read_not_payed_active_tour_applications()
        except Exception as e:
            raise e

    @staticmethod
    def update_tour_application_is_payed_status(tour_app_id: str, is_payed: bool):
        try:
            with SessionLocal() as db:
                tour_application_repository = TourApplicationRepository(db)
                return tour_application_repository.update_tour_application_is_payed_status(tour_app_id, is_payed)
        except Exception as e:
            raise e

    @staticmethod
    def update_tour_application_is_active_status(tour_app_id: str, is_active: bool):
        try:
            with SessionLocal() as db:
                tour_application_repository = TourApplicationRepository(db)
                return tour_application_repository.update_tour_application_is_active_status(tour_app_id, is_active)
        except Exception as e:
            raise e

    @staticmethod
    def change_customer_on_tour_application(tour_app_id: str, customer_id: str):
        try:
            with SessionLocal() as db:
                tour_application_repository = TourApplicationRepository(db)
                return tour_application_repository.change_customer_on_tour_application(tour_app_id, customer_id)
        except Exception as e:
            raise e

    @staticmethod
    def delete_tour_application_by_id(tour_app_id: str):
        try:
            with SessionLocal() as db:
                tour_application_repository = TourApplicationRepository(db)
                return tour_application_repository.delete_tour_application_by_id(tour_app_id)
        except Exception as e:
            raise e
