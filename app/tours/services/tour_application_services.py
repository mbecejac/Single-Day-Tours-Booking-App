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
                # check if tour exists
                tour_check = tour_repository.read_tour_by_id(tour_id)
                # check if customer exists
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
    def count_number_of_applications_by_tour_id(tour_id: str):
        try:
            with SessionLocal() as db:
                tour_application_repository = TourApplicationRepository(db)
                return tour_application_repository.count_number_of_applications_by_tour_id(tour_id)
        except Exception as e:
            raise e

    @staticmethod
    def sort_tours_by_number_of_applications_desc():
        try:
            with SessionLocal() as db:
                tours_repository = TourRepository(db)
                tour_application_repository = TourApplicationRepository(db)
                tours = tours_repository.read_all_tours()
                tours_with_num_of_apps = []
                for tour in tours:
                    num_of_application = tour_application_repository.count_number_of_applications_by_tour_id(tour.id)
                    tours_with_num_of_apps.append([tour.id, tour.tour_name, tour.tour_date, num_of_application])
                return sorted(tours_with_num_of_apps, key=lambda x: x[3], reverse=True)
        except Exception as e:
            raise e

    @staticmethod
    def get_passenger_list_by_tour_id(tour_id: str):
        try:
            with SessionLocal() as db:
                tour_application_repository = TourApplicationRepository(db)
                applications = tour_application_repository.read_all_tour_applications_by_tour_id(tour_id)
                passenger_list = []
                for application in applications:
                    passenger_list.append(
                        [
                            application.customer_id,
                            application.customer.name,
                            application.customer.last_name,
                            application.customer.phone_number,
                        ]
                    )
                return passenger_list
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
