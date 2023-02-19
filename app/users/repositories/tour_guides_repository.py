from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.users.exceptions import TourGuideExceptionName, TourGuideNotFoundException, UserNotFoundException
from app.users.models import TourGuide


class TourGuideRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_tour_guide(self, name: str, last_name: str, phone_number: str, user_id: str, language_id: str):
        try:
            tour_guide = TourGuide(name, last_name, phone_number, user_id, language_id)
            self.db.add(tour_guide)
            self.db.commit()
            self.db.refresh(tour_guide)
            return tour_guide
        except IntegrityError as e:
            raise e
        except Exception as e:
            raise e

    def read_all_tour_guides(self):
        return self.db.query(TourGuide).all()

    def read_tour_guide_by_id(self, tour_guide_id: str):
        tour_guide = self.db.query(TourGuide).filter(TourGuide.id == tour_guide_id).first()
        if tour_guide is None:
            raise TourGuideNotFoundException(
                message=f"Tour guide with provided id: {tour_guide_id} not found", code=400
            )
        return tour_guide

    def read_tour_guide_by_user_id(self, user_id: str):
        tour_guide = self.db.query(TourGuide).filter(TourGuide.user_id == user_id).first()
        if tour_guide is None:
            raise UserNotFoundException(message=f"Tour guide with provided user id: {user_id} not found", code=400)
        return tour_guide

    def read_tour_guide_by_name_or_lastname(self, name_lastname: str):
        try:
            tour_guides = (
                self.db.query(TourGuide).filter(TourGuide.name.ilike(f"%{name_lastname}%")).all()
                or self.db.query(TourGuide).filter(TourGuide.last_name.ilike(f"%{name_lastname}%")).all()
            )
            if tour_guides is None:
                raise TourGuideExceptionName(
                    message=f"Tour guide with provided name or last name: {name_lastname} not found", code=400
                )
            return tour_guides
        except Exception as e:
            raise e

    def update_tour_guide_data(
        self, tour_guide_id: str, name: str = None, last_name: str = None, phone_number: str = None
    ):
        try:
            tour_guide = self.db.query(TourGuide).filter(TourGuide.id == tour_guide_id).first()
            if tour_guide is None:
                raise TourGuideNotFoundException(
                    message=f"Tour guide with provided id: {tour_guide_id} not found", code=400
                )
            if name is not None:
                tour_guide.name = name
            if last_name is not None:
                tour_guide.last_name = last_name
            if phone_number is not None:
                tour_guide.phone_number = phone_number
            self.db.add(tour_guide)
            self.db.commit()
            self.db.refresh(tour_guide)
            return tour_guide
        except Exception as e:
            raise e

    def update_tour_guide_language_id(self, tour_guide_id: str, language_id: str):
        try:
            tour_guide = self.db.query(TourGuide).filter(TourGuide.id == tour_guide_id).first()
            if tour_guide is None:
                raise TourGuideNotFoundException(
                    message=f"Tour guide with provided id: {tour_guide_id} not found", code=400
                )
            if language_id is not None:
                tour_guide.language_id = language_id
            self.db.add(tour_guide)
            self.db.commit()
            self.db.refresh(tour_guide)
            return tour_guide
        except Exception as e:
            raise e

    def update_tour_guide_is_employee(self, tour_guide_id: str):
        try:
            tour_guide = self.db.query(TourGuide).filter(TourGuide.id == tour_guide_id).first()
            if tour_guide is None:
                raise TourGuideNotFoundException(
                    message=f"Tour guide with provided id: {tour_guide_id} not found", code=400
                )
            tour_guide.is_employee = 1
            self.db.add(tour_guide)
            self.db.commit()
            self.db.refresh(tour_guide)
            return tour_guide
        except Exception as e:
            raise e

    def delete_tour_guide_by_id(self, tour_guide_id: str):
        try:
            tour_guide = self.db.query(TourGuide).filter(TourGuide.id == tour_guide_id).first()
            if tour_guide is None:
                raise TourGuideNotFoundException(
                    message=f"Tour guide with provided id: {tour_guide_id} not found", code=400
                )
            self.db.delete(tour_guide)
            self.db.commit()
            return True
        except Exception as e:
            raise e
