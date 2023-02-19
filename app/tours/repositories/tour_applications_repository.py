from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.tours.exceptions import (
    TourApplicationExceptionActive,
    TourApplicationExceptionCustomer,
    TourApplicationNotFoundException,
)
from app.tours.models import TourApplication


class TourApplicationRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_tour_application(self, customer_id: str, tour_id: str):
        try:
            tour_application = TourApplication(customer_id, tour_id)
            self.db.add(TourApplication)
            self.db.commit()
            self.db.refresh(TourApplication)
            return tour_application
        except IntegrityError as e:
            raise e
        except Exception as e:
            raise e

    def read_all_tour_applications(self):
        return self.db.query(TourApplication).limit(20).all()

    def read_tour_application_by_id(self, tour_app_id: str):
        tour_application = self.db.query(TourApplication).filter(TourApplication.id == tour_app_id).limit(20).all()
        if tour_application is None:
            raise TourApplicationNotFoundException(
                message=f"Tour application with provided ID: {tour_app_id} not found.", code=400
            )
        return tour_application

    def read_all_active_tour_applications(self):
        tour_applications = self.db.query(TourApplication).filter(TourApplication.is_active == 1).limit(20).all()
        if not tour_applications:
            raise TourApplicationExceptionActive(message="No active tour applications", code=400)
        return tour_applications

    def read_all_tour_applications_by_customer_id(self, customer_id: str):
        tour_applications = (
            self.db.query(TourApplication).filter(TourApplication.customer_id == customer_id).limit(20).all()
        )
        if not tour_applications:
            raise TourApplicationExceptionCustomer(
                message=f"Tour application with provided Customer ID: {customer_id} not found-", code=400
            )
        return tour_applications

    def read_all_tour_applications_by_tour_id(self, tour_id: str):
        tour_applications = self.db.query(TourApplication).filter(TourApplication.tour_id == tour_id).limit(20).all()
        if not tour_applications:
            raise TourApplicationExceptionCustomer(
                message=f"Tour application with provided Tour ID: {tour_id} not found-", code=400
            )
        return tour_applications

    def read_not_payed_active_tour_applications(self):
        tour_applications = (
            self.db.query(TourApplication).filter(TourApplication.is_payed == 0).all()
            and self.db.query(TourApplication).filter(TourApplication.is_active == 1).all()
        )
        if not tour_applications:
            raise TourApplicationExceptionActive(message="Not found active not payed tour applications", code=400)
        return tour_applications

    def update_tour_application_is_payed_status(self, tour_app_id: str, is_payed: bool):
        try:
            tour_application = self.db.query(TourApplication).filter(TourApplication.id == tour_app_id).first()
            if tour_application is None:
                raise TourApplicationNotFoundException(
                    message=f"Tour application with provided id: {tour_app_id} not found.", code=400
                )

            tour_application.is_payed = is_payed
            self.db.add(tour_application)
            self.db.commit()
            self.db.refresh(tour_application)
            return tour_application
        except Exception as e:
            raise e

    def update_tour_application_is_active_status(self, tour_app_id: str, is_active: bool):
        try:
            tour_application = self.db.query(TourApplication).filter(TourApplication.id == tour_app_id).first()
            if tour_application is None:
                raise TourApplicationNotFoundException(
                    message=f"Tour application with provided id: {tour_app_id} not found.", code=400
                )

            tour_application.is_active = is_active
            self.db.add(tour_application)
            self.db.commit()
            self.db.refresh(tour_application)
            return tour_application
        except Exception as e:
            raise e

    def change_customer_on_tour_application(self, tour_app_id: str, customer_id: str):
        try:
            tour_application = self.db.query(TourApplication).filter(TourApplication.id == tour_app_id).first()
            if tour_application is None:
                raise TourApplicationNotFoundException(
                    message=f"Tour application with provided id: {tour_app_id} not found.", code=400
                )

            tour_application.customer_id = customer_id
            self.db.add(tour_application)
            self.db.commit()
            self.db.refresh(tour_application)
            return tour_application
        except Exception as e:
            raise e

    def delete_tour_application_by_id(self, tour_app_id: str):
        try:
            tour_application = self.db.query(TourApplication).filter(TourApplication.id == tour_app_id).first()
            if tour_application is None:
                raise TourApplicationNotFoundException(
                    message=f"Tour application with provided id: {tour_app_id} not found.", code=400
                )
            self.db.delete(tour_application)
            self.db.commit()
            return True
        except Exception as e:
            raise e
