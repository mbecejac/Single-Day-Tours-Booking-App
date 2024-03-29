from app.db import SessionLocal
from app.tours.exceptions import BusCarrierNotFoundException, TourExceptionLanguage, TourNotFoundException
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
        bus_carrier_id: str = "b3919fc4-8820-4f3f-b9e6-96dbed2b2783",  # default bus carrier id is for walking tour
    ):
        try:
            with SessionLocal() as db:
                tour_repository = TourRepository(db)
                tour_guide_repository = TourGuideRepository(db)
                # check if tour guide speaks the language provided for guiding the tour
                tour_guide_language_check = tour_guide_repository.read_tour_guide_by_id(tour_guide_id)
                language_name = tour_guide_language_check.language.language_name
                if tour_guide_language_check.language_id == tour_language:
                    return tour_repository.create_tour(
                        tour_name,
                        tour_date,
                        location,
                        description,
                        price,
                        is_walking_tour,
                        tour_language,
                        tour_guide_id,
                        bus_carrier_id,
                    )
                else:
                    raise TourExceptionLanguage(message=f"Tour guide is not speaking {language_name}", code=404)
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
    def read_active_tours_by_date_location_language_and_price(
        tour_date: str = None, location: str = None, price: float = 1000
    ):
        try:
            with SessionLocal() as db:
                tour_repository = TourRepository(db)
                return tour_repository.read_active_tours_by_date_location_language_and_price(tour_date, location)
        except Exception as e:
            raise e

    @staticmethod
    def read_tours_by_location_and_language(location: str, language: str):
        try:
            with SessionLocal() as db:
                tour_repository = TourRepository(db)
                tours_by_location = tour_repository.read_tours_by_location(location)
                tours_by_language = tour_repository.read_tours_by_tour_language(language)
                if location and language:
                    return list(set(tours_by_location) & set(tours_by_language))
                else:
                    raise TourNotFoundException(message="Tour not found", code=404)

        except Exception as e:
            raise e

    @staticmethod
    def read_tours_by_tour_guide_id(tour_guide_id: str):
        try:
            with SessionLocal() as db:
                tour_repository = TourRepository(db)
                return tour_repository.read_tours_by_tour_guide_id(tour_guide_id)
        except Exception as e:
            raise e

    @staticmethod
    def update_tour_guide_on_tour(tour_id: str, tour_guide_id: str):
        try:
            with SessionLocal() as db:
                tour_repository = TourRepository(db)
                tour_guide_repository = TourGuideRepository(db)
                tour = tour_repository.read_tour_by_id(tour_id)
                tour_guide_check = tour_guide_repository.read_tour_guide_by_id(tour_guide_id)
                tour_guide_language_check = tour_guide_repository.read_tour_guide_by_id(tour_guide_id)
                if (
                    tour_guide_check.id == tour_guide_id
                    and tour.tour_language == tour_guide_language_check.language.language_name
                ):
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
