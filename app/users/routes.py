from fastapi import APIRouter, Depends

from app.users.controllers import EmployeeController, JWTBearer, LanguageController, UserController
from app.users.schemas import (
    EmployeeSchema,
    EmployeeSchemaInput,
    LanguageSchema,
    LanguageSchemaInput,
    UserSchema,
    UserSchemaInput,
)

user_router = APIRouter(prefix="/api/users", tags=["Users"])


@user_router.post("/add-new-user", response_model=UserSchema)  # TODO Add dependencies JWTBearer(superuser)
def create_user(user: UserSchemaInput):
    return UserController.create_user(user.email, user.password)


@user_router.post("/add-new-super-user", response_model=UserSchema, dependencies=[Depends(JWTBearer("superuser"))])
def create_superuser(user: UserSchemaInput):
    return UserController.create_super_user(user.email, user.password)


@user_router.post("/login")
def user_login(user: UserSchemaInput):
    return UserController.login_user(user.email, user.password)


@user_router.get(
    "/get-all-users", response_model=list[UserSchema]
)  # TODO Add dependencies JWTBearer(superuser, employee)
def get_all_users():
    return UserController.get_all_users()


@user_router.get("/get-user/id", response_model=UserSchema)  # TODO Add dependencies JWTBearer(superuser, employee)
def get_user_by_id(user_id: str):
    return UserController.get_user_by_id(user_id)


@user_router.get("/get-user/email", response_model=UserSchema)  # TODO Add dependencies JWTBearer(superuser, employee)
def get_user_by_email(email: str):
    return UserController.get_user_by_email(email)


@user_router.put("/update/is-active", response_model=UserSchema, dependencies=[Depends(JWTBearer("superuser"))])
def update_user_is_active(user_id: str, is_active: bool):
    return UserController.update_user_is_active(user_id, is_active)


@user_router.put("/update/is-superuser", response_model=UserSchema, dependencies=[Depends(JWTBearer("superuser"))])
def update_user_is_superuser(user_id: str, is_superuser: bool):
    return UserController.update_user_is_superuser(user_id, is_superuser)


@user_router.delete("/")  # TODO Add dependencies JWTBearer(superuser)
def delete_user_by_id(user_id: str):
    return UserController.delete_user_by_id(user_id)


employee_router = APIRouter(prefix="/api/employees", tags=["Employees"])


@employee_router.post("/add-new-employee", response_model=EmployeeSchema)  # TODO Add dependencies JWTBearer(superuser)
def create_employee(employee: EmployeeSchemaInput):
    return EmployeeController.create_employee(employee.user_id)


@employee_router.get(
    "/get-all-employees", response_model=list[EmployeeSchema]
)  # TODO Add dependencies JWTBearer(superuser, employee)
def get_all_employees():
    return EmployeeController.get_all_employees()


@employee_router.get(
    "/get-employee/id", response_model=EmployeeSchema
)  # TODO Add dependencies JWTBearer(superuser, employee)
def get_employee_by_id(employee_id: int):
    return EmployeeController.get_employee_by_id(employee_id)


@employee_router.get(
    "/get-employee/user-id", response_model=EmployeeSchema
)  # TODO Add dependencies JWTBearer(superuser, employee)
def get_employee_by_user_id(user_id: str):
    return EmployeeController.get_employee_by_user_id(user_id)


@employee_router.delete("/")  # TODO Add dependencies JWTBearer(superuser)
def delete_employee_by_id(employee_id):
    return EmployeeController.delete_employee_by_id(employee_id)


language_router = APIRouter(prefix="/api/languages", tags=["Languages"])


@language_router.post("/add-new-language", response_model=LanguageSchema)  # TODO Add dependencies JWTBearer(superuser)
def create_language(language: LanguageSchemaInput):
    return LanguageController.create_language(language.language_name)


@language_router.get(
    "/get-all-languages", response_model=list[LanguageSchema]
)  # TODO Add dependencies JWTBearer(superuser, employee)
def get_all_languages():
    return LanguageController.get_all_languages()


@language_router.get(
    "/get-language-by-id", response_model=LanguageSchema
)  # TODO Add dependencies JWTBearer(superuser, employee)
def get_language_by_id(language_id: str):
    return LanguageController.get_language_by_id(language_id)


@language_router.delete("/")  # TODO Add dependencies JWTBearer(superuser)
def delete_language_by_id(language_id: str):
    return LanguageController.delete_language_by_id(language_id)
