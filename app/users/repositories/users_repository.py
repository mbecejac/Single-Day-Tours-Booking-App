"""User related repositories"""
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.users.exceptions import UserNotFoundException
from app.users.models import User


class UserRepository:
    """Repository for User management."""

    def __init__(self, db: Session):
        """
        Initialize the UserRepository with a database connection.

        :param db: Session instance for database connection
        :type db: Session
        """
        self.db = db

    def create_user(self, email, password):
        """Create a new user."""
        try:
            user = User(email, password)
            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)
            return user
        except IntegrityError as e:
            raise e
        except Exception as e:
            raise e

    def create_super_user(self, email, password):
        """Create a new superuser."""
        try:
            user = User(email=email, password=password, is_superuser=True)
            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)
            return user
        except IntegrityError as e:
            raise e

    def read_all_users(self):
        """Read all the users in the database."""
        return self.db.query(User).all()

    def read_user_by_id(self, user_id: str):
        """Read a user by id."""
        user = self.db.query(User).filter(User.id == user_id).first()
        if user is None:
            raise UserNotFoundException(message=f"User with provided id: {user_id} not found", code=400)
        return user

    def read_user_by_email(self, email: str):
        """Read a user by email."""
        user = self.db.query(User).filter(User.email == email).first()
        if user is None:
            raise UserNotFoundException(message=f"User with provided email: {email} not found", code=400)
        return user

    def update_user_is_active(self, user_id: str, is_active: bool):
        """Update is_active status of a user."""
        try:
            user = self.db.query(User).filter(User.id == user_id).first()
            user.is_active = is_active
            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)
            return user
        except Exception as e:
            raise e

    def update_user_is_superuser(self, user_id: str, is_superuser: bool):
        """Update is_superuser status of a user."""
        try:
            user = self.db.query(User).filter(User.id == user_id).first()
            user.is_superuser = is_superuser
            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)
            return user
        except Exception as e:
            raise e

    def delete_user_by_id(self, user_id: str):
        """Delete user by id."""
        try:
            user = self.db.query(User).filter(User.id == user_id).first()
            if user is None:
                raise UserNotFoundException(message=f"Users with provided id: {user_id} not found.", code=400)
            self.db.delete(user)
            self.db.commit()
            return True
        except Exception as e:
            raise e
