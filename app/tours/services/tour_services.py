from app.db import SessionLocal
from app.tours.exceptions import BusCarrierNotFoundException
from app.tours.repositories import BusCarrierRepository, TourRepository
from app.users.exceptions import TourGuideNotFoundException
from app.users.repositories import TourGuideRepository


class TourService:
    @staticmethod
    def create_tour(
        tour_name: str,
        tour_date: str,
        location: str,
        description: str,
        price: float,
        is_walking_tour: bool,
        tour_language: str,
        tour_guide_id: str,
    ):
        try:
            with SessionLocal() as db:
                tour_repository = TourRepository(db)
                return tour_repository.create_tour(
                    tour_name, tour_date, location, description, price, is_walking_tour, tour_language, tour_guide_id
                )
        except Exception as e:
            raise e

    @staticmethod
    def read_all_tours():
        try:
            with SessionLocal() as db:
                tour_repository = TourRepository(db)
                return tour_repository.read_all_tours()
        except Exception as e:
            raise e

    @staticmethod
    def read_tour_by_id(tour_id: str):
        try:
            with SessionLocal() as db:
                tour_repository = TourRepository(db)
                return tour_repository.read_tour_by_id(tour_id)
        except Exception as e:
            raise e

    @staticmethod
    def read_tours_by_date(tour_date: str):
        try:
            with SessionLocal() as db:
                tour_repository = TourRepository(db)
                return tour_repository.read_tours_by_date(tour_date)
        except Exception as e:
            raise e

    @staticmethod
    def read_tours_by_location(location: str):
        try:
            with SessionLocal() as db:
                tour_repository = TourRepository(db)
                return tour_repository.read_tours_by_location(location)
        except Exception as e:
            raise e

    @staticmethod
    def read_tours_by_max_price(price: float):
        try:
            with SessionLocal() as db:
                tour_repository = TourRepository(db)
                return tour_repository.read_tours_by_max_price(price)
        except Exception as e:
            raise e

    @staticmethod
    def read_walking_tours():
        try:
            with SessionLocal() as db:
                tour_repository = TourRepository(db)
                return tour_repository.read_walking_tours()
        except Exception as e:
            raise e

    @staticmethod
    def read_tours_by_tour_language(language: str):
        try:
            with SessionLocal() as db:
                tour_repository = TourRepository(db)
                return tour_repository.read_tours_by_tour_language(language)
        except Exception as e:
            raise e

    @staticmethod
    def read_active_tours():
        try:
            with SessionLocal() as db:
                tour_repository = TourRepository(db)
                return tour_repository.read_active_tours()
        except Exception as e:
            raise e

    @staticmethod
    def update_tour_guide_on_tour(tour_id: str, tour_guide_id: str):
        try:
            with SessionLocal() as db:
                tour_repository = TourRepository(db)
                tour_guide_repository = TourGuideRepository(db)
                tour_guide_check = tour_guide_repository.read_tour_guide_by_id(tour_guide_id)
                if tour_guide_check.id == tour_guide_id:
                    return tour_repository.update_tour_guide_on_tour(tour_id, tour_guide_id)
                else:
                    raise TourGuideNotFoundException(message=f"Tour guide with ID: {tour_guide_id} not found", code=404)
        except Exception as e:
            raise e

    @staticmethod
    def update_bus_carrier_on_tour(tour_id: str, bus_carrier_id: str):
        try:
            with SessionLocal() as db:
                tour_repository = TourRepository(db)
                bus_carrier_repository = BusCarrierRepository(db)
                bus_carrier_check = bus_carrier_repository.read_bus_carrier_by_id(bus_carrier_id)
                if bus_carrier_check.id == bus_carrier_id:
                    return tour_repository.update_bus_carrier_on_tour(tour_id, bus_carrier_id)
                else:
                    raise BusCarrierNotFoundException(
                        message=f"Bus carrier with ID: {bus_carrier_id} not found", code=404
                    )
        except Exception as e:
            raise e

    @staticmethod
    def update_tour_is_active(tour_id: str, is_active: bool):
        try:
            with SessionLocal() as db:
                tour_repository = TourRepository(db)
                return tour_repository.update_tour_is_active(tour_id, is_active)
        except Exception as e:
            raise e

    @staticmethod
    def delete_tour_by_id(tour_id: str):
        try:
            with SessionLocal() as db:
                tour_repository = TourRepository(db)
                tour_repository.delete_tour_by_id(tour_id)
                return True
        except Exception as e:
            raise e
