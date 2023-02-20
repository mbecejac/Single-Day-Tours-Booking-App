from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.tours.exceptions import (
    TourExceptionActive,
    TourExceptionDate,
    TourExceptionLanguage,
    TourExceptionLocation,
    TourExceptionPrice,
    TourExceptionWalkingTour,
    TourNotFoundException,
)
from app.tours.models import Tour


class TourRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_tour(
        self,
        tour_name: str,
        tour_date: str,
        location: str,
        description: str,
        price: float,
        is_walking_tour: bool,
        tour_language: str,
        tour_guide_id: str,
        bus_carrier_id: str,
    ):
        try:
            tour = Tour(
                tour_name=tour_name,
                tour_date=tour_date,
                location=location,
                description=description,
                price=price,
                is_walking_tour=is_walking_tour,
                tour_language=tour_language,
                tour_guide_id=tour_guide_id,
                bus_carrier_id=bus_carrier_id,
            )
            self.db.add(tour)
            self.db.commit()
            self.db.refresh(tour)
            return tour
        except IntegrityError as e:
            raise e
        except Exception as e:
            raise e

    def read_all_tours(self):
        return self.db.query(Tour).limit(20).all()

    def read_tour_by_id(self, tour_id: str):
        tour = self.db.query(Tour).filter(Tour.id == tour_id).first()
        if tour is None:
            raise TourNotFoundException(message=f"Tour with provided ID: {tour_id} not found.", code=400)
        return tour

    def read_tours_by_date(self, tour_date: str):
        tours = self.db.query(Tour).filter(Tour.tour_date == tour_date).limit(20).all()
        if not tours:
            raise TourExceptionDate(message=f"Tour with provided date: {tour_date} not found.", code=400)
        return tours

    def read_tours_by_location(self, location: str):
        tours = self.db.query(Tour).filter(Tour.location.ilike(f"%{location}%")).limit(20).all()
        if not tours:
            raise TourExceptionLocation(message=f"Tour for location: {location} not found.", code=400)
        return tours

    def read_tours_by_max_price(self, price: float):
        tours = self.db.query(Tour).filter(Tour.price <= price).limit(20).all()
        if not tours:
            raise TourExceptionPrice(message=f"Tour with provided max price: {price} not found.", code=400)
        return tours

    def read_walking_tours(self):
        tours = self.db.query(Tour).filter(Tour.is_walking_tour == 1).limit(20).all()
        if not tours:
            raise TourExceptionWalkingTour(message="Walking tour not found.", code=400)
        return tours

    def read_tours_by_tour_language(self, language: str):
        tours = self.db.query(Tour).filter(Tour.tour_language.ilike(f"%{language}%")).limit(20).all()
        if not tours:
            raise TourExceptionLanguage(message=f"Tour language: {language} not found.", code=400)
        return tours

    def read_active_tours(self):
        tours = self.db.query(Tour).filter(Tour.is_active == 1).limit(20).all()
        if not tours:
            raise TourExceptionActive(message="Not active tours found.", code=400)
        return tours

    def read_active_tours_by_date_location_language_and_price(
        self, tour_date: str = None, location: str = None, language: str = None, price: float = None
    ):
        tours = (
            self.db.query(Tour).filter(Tour.tour_date == tour_date).all()
            and self.db.query(Tour).filter(Tour.location.ilike(f"%{location}%")).all()
            and self.db.query(Tour).filter(Tour.price <= price).all()
            and self.db.query(Tour).filter(Tour.tour_language.ilike(f"%{language}%")).all()
            and self.db.query(Tour).filter(Tour.is_active == 1).all()
        )
        if not tours:
            raise TourExceptionActive(message="Not active tours found.", code=400)
        return tours

    def read_tours_by_tour_guide_id(self, tour_guide_id: str):
        tours = self.db.query(Tour).filter(Tour.tour_guide_id == tour_guide_id).limit(20).all()
        if not tours:
            raise TourNotFoundException(
                message=f"Tours guided by tour guide provided ID: {tour_guide_id} not found.", code=400
            )
        return tours

    def update_tour_guide_on_tour(self, tour_id: str, tour_guide_id: str = None):
        try:
            tour = self.db.query(Tour).filter(Tour.id == tour_id).first()
            if tour is None:
                raise TourNotFoundException(message=f"Tour with provided id: {tour_id} not found", code=400)
            if tour_guide_id is not None:
                tour.tour_guide_id = tour_guide_id
            self.db.add(tour)
            self.db.commit()
            self.db.refresh(tour)
            return tour
        except Exception as e:
            raise e

    def update_bus_carrier_on_tour(self, tour_id: str, bus_carrier_id: str = None):
        try:
            tour = self.db.query(Tour).filter(Tour.id == tour_id).first()
            if tour is None:
                raise TourNotFoundException(message=f"Tour with provided id: {tour_id} not found", code=400)
            if bus_carrier_id is not None:
                tour.bus_carrier_id = bus_carrier_id
            self.db.add(tour)
            self.db.commit()
            self.db.refresh(tour)
            return tour
        except Exception as e:
            raise e

    def update_tour_is_active(self, tour_id: str, is_active: bool):
        try:
            tour = self.db.query(Tour).filter(Tour.id == tour_id).first()
            if tour is None:
                raise TourNotFoundException(message=f"Tour with provided id: {tour_id} not found", code=400)

            tour.is_active = is_active
            self.db.add(tour)
            self.db.commit()
            self.db.refresh(tour)
            return tour
        except Exception as e:
            raise e

    def delete_tour_by_id(self, tour_id: str):
        try:
            tour = self.db.query(Tour).filter(Tour.id == tour_id).first()
            if tour is None:
                raise TourNotFoundException(message=f"Tour with provided ID: {tour_id} not found.", code=400)
            self.db.delete(tour)
            self.db.commit()
            return True
        except Exception as e:
            raise e
