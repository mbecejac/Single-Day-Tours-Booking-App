from fastapi import HTTPException, Response

from app.users.exceptions import LanguageNotFoundException, TourGuideExistsException, TourGuideNotFoundException
from app.users.services import TourGuideService


class TourGuideController:
    @staticmethod
    def create_tour_guide(name: str, last_name: str, phone_number: str, user_id: str, language_id: str):
        try:
            tour_guide = TourGuideService.create_tour_guide(name, last_name, phone_number, user_id, language_id)
            return tour_guide
        except TourGuideExistsException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_all_tour_guides():
        return TourGuideService.read_all_tour_guides()

    @staticmethod
    def get_tour_guide_by_id(tour_guide_id: str):
        try:
            tour_guide = TourGuideService.read_tour_guide_by_id(tour_guide_id)
            return tour_guide
        except TourGuideNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_tour_guide_by_user_id(user_id: str):
        try:
            tour_guide = TourGuideService.read_tour_guide_by_user_id(user_id)
            return tour_guide
        except TourGuideNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_tour_guide_by_name_or_last_name(name_lastname: str):
        try:
            tour_guide = TourGuideService.read_tour_guide_by_name_or_last_name(name_lastname)
            return tour_guide
        except TourGuideNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def update_tour_guide_data(tour_guide_id: str, name: str = None, last_name: str = None, phone_number: str = None):
        try:
            tour_guide = TourGuideService.update_tour_guide_data(tour_guide_id, name, last_name, phone_number)
            return tour_guide
        except TourGuideNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def update_tour_guide_language(tour_guide_id: str, language_id: str):
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
        try:
            tour_guide = TourGuideService.update_tour_guide_is_employee(tour_guide_id, is_employee)
            return tour_guide
        except TourGuideNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def delete_tour_guide_by_id(tour_guide_id: str):
        try:
            if TourGuideService.delete_tour_guide_by_id(tour_guide_id):
                return Response(content=f"Tour guide with ID: {tour_guide_id} deleted.", status_code=200)
        except TourGuideNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
