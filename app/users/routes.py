from fastapi import APIRouter

from app.users.controllers import UserController
from app.users.schemas import UserSchema, UserSchemaInput

user_router = APIRouter(prefix="/api/users", tags=["users"])


@user_router.post("/add-new-user", response_model=UserSchema)
def create_user(user: UserSchemaInput):
    return UserController.create_user(user.email, user.password)


@user_router.post("/add-new-super-user", response_model=UserSchema)
def create_superuser(user: UserSchemaInput):
    return UserController.create_super_user(user.email, user.password)


@user_router.post("/login")
def user_login(user: UserSchemaInput):
    return UserController.login_user(user.email, user.password)


@user_router.get("/get-all-users", response_model=list[UserSchema])
def get_all_users():
    return UserController.get_all_users()


@user_router.get("/id", response_model=UserSchema)
def get_user_by_id(user_id: str):
    return UserController.get_user_by_id(user_id)


@user_router.put("/update/is-active", response_model=UserSchema)
def update_user_is_active(user_id: str, is_active: bool):
    return UserController.update_user_is_active(user_id, is_active)


@user_router.put("/update/is-superuser", response_model=UserSchema)
def update_user_is_superuser(user_id: str, is_superuser: bool):
    return UserController.update_user_is_superuser(user_id, is_superuser)


@user_router.delete("/")
def delete_user_by_id(user_id: str):
    return UserController.delete_user_by_id(user_id)
