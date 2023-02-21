"""Tour guide related controllers"""
from fastapi import HTTPException, Response

from app.users.exceptions import LanguageNotFoundException, TourGuideExistsException, TourGuideNotFoundException
from app.users.services import TourGuideService


class TourGuideController:
    """Controller for tour guide management"""

    @staticmethod
    def create_tour_guide(name: str, last_name: str, phone_number: str, user_id: str, language_id: str):
        """Create a new tour guide"""
        try:
            tour_guide = TourGuideService.create_tour_guide(name, last_name, phone_number, user_id, language_id)
            return tour_guide
        except TourGuideExistsException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_all_tour_guides():
        """Get all tour guides"""
        return TourGuideService.read_all_tour_guides()

    @staticmethod
    def get_tour_guide_by_id(tour_guide_id: str):
        """Get tour guide by provided id"""
        try:
            tour_guide = TourGuideService.read_tour_guide_by_id(tour_guide_id)
            return tour_guide
        except TourGuideNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_tour_guide_by_user_id(user_id: str):
        """Get tour guide by provided user id"""
        try:
            tour_guide = TourGuideService.read_tour_guide_by_user_id(user_id)
            return tour_guide
        except TourGuideNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_tour_guide_by_name_or_last_name(name_lastname: str):
        """Get tour guide by provided name or last name"""
        try:
            tour_guide = TourGuideService.read_tour_guide_by_name_or_last_name(name_lastname)
            return tour_guide
        except TourGuideNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def update_tour_guide_data(tour_guide_id: str, name: str = None, last_name: str = None, phone_number: str = None):
        """Update tour guide data: name, last_name, phone_number."""
        try:
            tour_guide = TourGuideService.update_tour_guide_data(tour_guide_id, name, last_name, phone_number)
            return tour_guide
        except TourGuideNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def update_tour_guide_language(tour_guide_id: str, language_id: str):
        """Update tour guide language."""
        try:
            tour_guide = TourGuideService.update_tour_guide_language(tour_guide_id, language_id)
            return tour_guide
        except TourGuideNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except LanguageNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def update_tour_guide_is_employee(tour_guide_id: str, is_employee: bool):
        """Update tour guide is_employee status."""
        try:
            tour_guide = TourGuideService.update_tour_guide_is_employee(tour_guide_id, is_employee)
            return tour_guide
        except TourGuideNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def delete_tour_guide_by_id(tour_guide_id: str):
        """Delete tour guide by provided id"""
        try:
            if TourGuideService.delete_tour_guide_by_id(tour_guide_id):
                return Response(content=f"Tour guide with ID: {tour_guide_id} deleted.", status_code=200)
        except TourGuideNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
