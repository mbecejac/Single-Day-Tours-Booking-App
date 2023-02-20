from fastapi import HTTPException, Response

from app.tours.exceptions import (
    TourExceptionActive,
    TourExceptionDate,
    TourExceptionLanguage,
    TourExceptionLocation,
    TourExceptionPrice,
    TourExceptionTourGuide,
    TourExceptionWalkingTour,
    TourNotFoundException,
)
from app.tours.services import TourService


class TourController:
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
            tour = TourService.create_tour(
                tour_name, tour_date, location, description, price, is_walking_tour, tour_language, tour_guide_id
            )
            return tour
        except TourExceptionLanguage as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_all_tours():
        return TourService.read_all_tours()

    @staticmethod
    def get_tour_by_id(tour_id: str):
        try:
            tour = TourService.read_tour_by_id(tour_id)
            return tour
        except TourNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_tours_by_date(date: str):
        try:
            tours = TourService.read_tours_by_date(date)
            return tours
        except TourExceptionDate as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_tours_by_location(location: str):
        try:
            tours = TourService.read_tours_by_location(location)
            return tours
        except TourExceptionLocation as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_tours_by_max_price(price: float):
        try:
            tours = TourService.read_tours_by_max_price(price)
            return tours
        except TourExceptionPrice as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_walking_tours():
        try:
            tours = TourService.read_walking_tours()
            return tours
        except TourExceptionWalkingTour as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_tours_by_tour_language(language: str):
        try:
            tours = TourService.read_tours_by_tour_language(language)
            return tours
        except TourExceptionLanguage as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_active_tours():
        try:
            tours = TourService.read_active_tours()
            return tours
        except TourExceptionActive as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_active_tours_by_date_location_language_and_price(
        tour_date: str, location: str, language: str, price: float
    ):
        try:
            tours = TourService.read_active_tours_by_date_location_language_and_price(
                tour_date, location, language, price
            )
            return tours
        except TourExceptionActive as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_tour_by_tour_guide_id(tour_guide_id: str):
        try:
            tour = TourService.read_tours_by_tour_guide_id(tour_guide_id)
            return tour
        except TourExceptionTourGuide as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def update_tour_guide_on_tour(tour_id: str, tour_guide_id: str):
        try:
            tour = TourService.update_tour_guide_on_tour(tour_id, tour_guide_id)
            return tour
        except TourNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except TourExceptionLanguage as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def update_bus_carrier_on_tour(tour_id: str, bus_carrier_id: str):
        try:
            tour = TourService.update_bus_carrier_on_tour(tour_id, bus_carrier_id)
            return tour
        except TourNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def update_tour_is_active(tour_id: str, is_active: bool):
        try:
            tour = TourService.update_tour_is_active(tour_id, is_active)
            return tour
        except TourNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def delete_tour_by_id(tour_id: str):
        try:
            if TourService.delete_tour_by_id(tour_id):
                return Response(content=f"Tour with ID: {tour_id} deleted.", status_code=200)
        except TourNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
