from fastapi import HTTPException, Response

from app.tours.exceptions import (
    TourApplicationExceptionActive,
    TourApplicationExceptionCustomer,
    TourApplicationExceptionTour,
    TourApplicationNotFoundException,
    TourNotFoundException,
)
from app.tours.services import TourApplicationService
from app.users.exceptions import CustomerNotFoundException


class TourApplicationController:
    @staticmethod
    def create_tour_application(customer_id: str, tour_id: str):
        try:
            tour_application = TourApplicationService.create_tour_application(customer_id, tour_id)
            return tour_application
        except TourNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except CustomerNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_all_tour_applications():
        return TourApplicationService.read_all_tour_applications()

    @staticmethod
    def get_tour_application_by_id(tour_app_id: str):
        try:
            tour_application = TourApplicationService.read_tour_application_by_id(tour_app_id)
            return tour_application
        except TourApplicationNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_all_active_tour_applications():
        try:
            tour_applications = TourApplicationService.read_all_active_tour_applications()
            return tour_applications
        except TourApplicationExceptionActive as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_all_tour_applications_by_customer_id(customer_id: str):
        try:
            tour_application = TourApplicationService.read_tour_applications_by_customer_id(customer_id)
            return tour_application
        except TourApplicationExceptionCustomer as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_all_tour_applications_by_tour_id(tour_id: str):
        try:
            tour_application = TourApplicationService.read_tour_applications_by_tour_id()
            return tour_application
        except TourApplicationExceptionTour as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_not_payed_active_tour_applications():
        try:
            tour_applications = TourApplicationService.read_not_payed_active_tour_applications()
            return tour_applications
        except TourApplicationExceptionActive as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def update_tour_application_is_payed_status(tour_app_id: str, is_payed: bool):
        try:
            tour_application = TourApplicationService.update_tour_application_is_payed_status(tour_app_id, is_payed)
            return tour_application
        except TourApplicationNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def update_tour_application_is_active_status(tour_app_id: str, is_active: bool):
        try:
            tour_application = TourApplicationService.update_tour_application_is_active_status(tour_app_id, is_active)
            return tour_application
        except TourApplicationNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def change_customer_on_tour_application(tour_app_id: str, customer_id: str):
        try:
            tour_application = TourApplicationService.change_customer_on_tour_application(tour_app_id, customer_id)
            return tour_application
        except TourApplicationNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except TourApplicationExceptionCustomer as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def delete_tour_application_by_id(tour_app_id: str):
        try:
            if TourApplicationService.delete_tour_application_by_id(tour_app_id):
                return Response(content=f"Tour application with ID: {tour_app_id} deleted.", status_code=200)
        except TourApplicationNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
