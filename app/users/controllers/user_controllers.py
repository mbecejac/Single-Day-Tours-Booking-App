from fastapi import HTTPException, Response
from sqlalchemy.exc import IntegrityError

from app.users.exceptions import UserInvalidPassword, UserNotFoundException
from app.users.services import UserService, sign_jwt


class UserController:
    @staticmethod
    def create_user(email: str, password: str):
        try:
            user = UserService.create_user(email, password)
            return user
        except IntegrityError:
            raise HTTPException(status_code=400, detail=f"User with provided email: {email} already exist.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=e.__str__())

    @staticmethod
    def create_super_user(email: str, password: str):
        try:
            super_user = UserService.create_super_user(email, password)
            return super_user
        except IntegrityError:
            raise HTTPException(status_code=400, detail=f"User with provided email: {email} already exist.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=e.__str__())

    @staticmethod
    def get_all_users():
        return UserService.read_all_users()

    @staticmethod
    def get_user_by_id(user_id: str):
        try:
            user = UserService.read_user_by_id(user_id)
            return user
        except UserNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=e.__str__())

    @staticmethod
    def get_user_by_email(email: str):
        try:
            user = UserService.read_user_by_email(email)
            return user
        except UserNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=e.__str__())

    @staticmethod
    def update_user_is_active(user_id: str, is_active: bool):
        try:
            UserService.update_user_is_active(user_id, is_active)
        except Exception as e:
            raise HTTPException(status_code=500, detail=e.__str__())

    @staticmethod
    def update_user_is_superuser(user_id: str, is_superuser: bool):
        try:
            UserService.update_user_is_superuser(user_id, is_superuser)
        except Exception as e:
            raise HTTPException(status_code=500, detail=e.__str__())

    @staticmethod
    def delete_user_by_id(user_id: str):
        try:
            UserService.delete_user_by_id(user_id)
            return Response(content=f"User with id: {user_id} is deleted")
        except Exception as e:
            raise HTTPException(status_code=400, detail=e.__str__())

    @staticmethod
    def login_user(email: str, password: str):
        try:
            user = UserService.login_user(email, password)
            if user.is_superuser:
                return sign_jwt(user.id, "superuser")
            return sign_jwt(user.id, "not_superuser")
        except UserInvalidPassword as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=e.__str__())
