"""User related controllers"""
from fastapi import HTTPException
from pydantic import EmailStr
from sqlalchemy.exc import IntegrityError

from app.users.exceptions import UserInvalidPassword, UserNotFoundException
from app.users.services import UserService, sign_jwt


class UserController:
    """Controller for user management"""

    @staticmethod
    def create_user(email: EmailStr, password: str):
        """Create a new user"""
        try:
            user = UserService.create_user(email, password)
            # EmailService.send_email_after_user_is_create(email)
            # Email service disabled temporarily. Raising Timed out, while waiting for server ready message
            return user
        except IntegrityError:
            raise HTTPException(status_code=400, detail=f"User with provided email: {email} already exist.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def create_super_user(email: str, password: str):
        """Create a new superuser"""
        try:
            super_user = UserService.create_super_user(email, password)
            return super_user
        except IntegrityError:
            raise HTTPException(status_code=400, detail=f"User with provided email: {email} already exist.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def login_user(email: str, password: str):
        """User login by email and password"""
        try:
            user = UserService.login_user(email, password)
            if user.is_superuser:
                return sign_jwt(user.id, "superuser")
            return sign_jwt(user.id, "common_user")
        except UserInvalidPassword as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_all_users():
        """Get all users"""
        return UserService.read_all_users()

    @staticmethod
    def get_user_by_id(user_id: str):
        """Get user by provided id"""
        try:
            user = UserService.read_user_by_id(user_id)
            return user
        except UserNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_user_by_email(email: str):
        """Get user by provided email"""
        try:
            user = UserService.read_user_by_email(email)
            return user
        except UserNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def update_user_is_active(user_id: str, is_active: bool):
        """Update user is_active status"""
        try:
            user = UserService.update_user_is_active(user_id, is_active)
            return user
        except UserNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=str(e))
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def update_user_is_superuser(user_id: str, is_superuser: bool):
        """Update user is_superuser status"""
        try:
            user = UserService.update_user_is_superuser(user_id, is_superuser)
            return user
        except UserNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=str(e))
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def delete_user_by_id(user_id: str):
        """Delete user by provided id"""
        try:
            UserService.delete_user_by_id(user_id)
            return {"message": f"User with id: {user_id} is deleted"}
        except UserNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
