"""User related services"""
import hashlib

from app.db import SessionLocal
from app.users.exceptions import UserInvalidPassword
from app.users.repositories import UserRepository


class UserService:
    """Service for user management"""

    @staticmethod
    def create_user(email: str, password: str):
        """Create a new user."""
        try:
            with SessionLocal() as db:
                user_repository = UserRepository(db)
                hashed_password = hashlib.sha256(bytes(password, "utf-8")).hexdigest()
                return user_repository.create_user(email, hashed_password)
        except Exception as e:
            raise e

    @staticmethod
    def create_super_user(email: str, password: str):
        """Create a new superuser"""
        try:
            with SessionLocal() as db:
                user_repository = UserRepository(db)
                hashed_password = hashlib.sha256(bytes(password, "utf-8")).hexdigest()
                return user_repository.create_super_user(email, hashed_password)
        except Exception as e:
            raise e

    @staticmethod
    def login_user(email: str, password: str):
        """User login by email and password"""
        try:
            with SessionLocal() as db:
                user_repository = UserRepository(db)
                user = user_repository.read_user_by_email(email)
                if hashlib.sha256(bytes(password, "utf-8")).hexdigest() != user.password:
                    raise UserInvalidPassword(message="Not valid password", code=401)
                return user
        except Exception as e:
            raise e

    @staticmethod
    def read_all_users():
        """Read all users"""
        try:
            with SessionLocal() as db:
                user_repository = UserRepository(db)
                return user_repository.read_all_users()
        except Exception as e:
            raise e

    @staticmethod
    def read_user_by_id(user_id: str):
        """Read user by provided id"""
        try:
            with SessionLocal() as db:
                user_repository = UserRepository(db)
                return user_repository.read_user_by_id(user_id)
        except Exception as e:
            raise e

    @staticmethod
    def read_user_by_email(email: str):
        """Read user by provided email."""
        try:
            with SessionLocal() as db:
                user_repository = UserRepository(db)
                return user_repository.read_user_by_email(email)
        except Exception as e:
            raise e

    @staticmethod
    def update_user_is_active(user_id: str, is_active: bool):
        """Update user is_active status"""
        try:
            with SessionLocal() as db:
                user_repository = UserRepository(db)
                return user_repository.update_user_is_active(user_id, is_active)
        except Exception as e:
            return e

    @staticmethod
    def update_user_is_superuser(user_id: str, is_superuser: bool):
        """Update user is_superuser status"""
        try:
            with SessionLocal() as db:
                user_repository = UserRepository(db)
                return user_repository.update_user_is_superuser(user_id, is_superuser)
        except Exception as e:
            return e

    @staticmethod
    def delete_user_by_id(user_id: str):
        """Delete user by provided user id"""
        try:
            with SessionLocal() as db:
                user_repository = UserRepository(db)
                return user_repository.delete_user_by_id(user_id)
        except Exception as e:
            raise e
