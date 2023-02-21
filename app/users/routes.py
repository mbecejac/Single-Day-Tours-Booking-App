from fastapi import APIRouter, Depends

from app.users.controllers import (
    CustomerController,
    EmployeeController,
    JWTBearer,
    LanguageController,
    TourGuideController,
    UserController,
)
from app.users.schemas import (
    CustomerSchema,
    CustomerSchemaInput,
    CustomerSchemaUpdate,
    EmployeeSchema,
    EmployeeSchemaInput,
    LanguageSchema,
    LanguageSchemaInput,
    TourGuideSchema,
    TourGuideSchemaInput,
    TourGuideSchemaIsEmployeeUpdate,
    TourGuideSchemaLanguageUpdate,
    TourGuideSchemaUpdate,
    UserSchema,
    UserSchemaInput,
    UserSchemaIsActiveUpdate,
    UserSchemaIsSuperuserUpdate,
)

user_router = APIRouter(prefix="/api/users", tags=["Users"])


@user_router.post("/add-new-user", response_model=UserSchema)  # TODO Add dependencies JWTBearer(superuser)
def create_user(user: UserSchemaInput):
    return UserController.create_user(user.email, user.password)


@user_router.post("/add-new-super-user", response_model=UserSchema)  # dependencies=[Depends(JWTBearer("superuser"))])
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
def update_user_is_active(user: UserSchemaIsActiveUpdate):
    return UserController.update_user_is_active(user.id, user.is_active)


@user_router.put("/update/is-superuser", response_model=UserSchema, dependencies=[Depends(JWTBearer("superuser"))])
def update_user_is_superuser(user: UserSchemaIsSuperuserUpdate):
    return UserController.update_user_is_superuser(user.id, user.is_superuser)


@user_router.delete("/delete-user")  # TODO Add dependencies JWTBearer(superuser)
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


@employee_router.delete("/delete-employee")  # TODO Add dependencies JWTBearer(superuser)
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


@language_router.delete("/delete-language")  # TODO Add dependencies JWTBearer(superuser)
def delete_language_by_id(language_id: str):
    return LanguageController.delete_language_by_id(language_id)


tour_guide_router = APIRouter(prefix="/api/tour-guides", tags=["Tour Guides"])


@tour_guide_router.post(
    "/add-new-tour-guide", response_model=TourGuideSchema
)  # TODO Add dependencies JWTBearer(superuser)
def create_tour_guide(tour_guide: TourGuideSchemaInput):
    return TourGuideController.create_tour_guide(
        tour_guide.name,
        tour_guide.last_name,
        tour_guide.phone_number,
        tour_guide.user_id,
        tour_guide.language_id,
    )


@tour_guide_router.get(
    "/get-all-tour-guides", response_model=list[TourGuideSchema]
)  # TODO Add dependencies JWTBearer(superuser, employee)
def get_all_tour_guides():
    return TourGuideController.get_all_tour_guides()


@tour_guide_router.get(
    "/get-tour-guide-by-id", response_model=TourGuideSchema
)  # TODO Add dependencies JWTBearer(superuser, employee)
def get_tour_guide_by_id(tour_guide_id: str):
    return TourGuideController.get_tour_guide_by_id(tour_guide_id)


@tour_guide_router.get(
    "/get-tour-guide-by-user-id", response_model=TourGuideSchema
)  # TODO Add dependencies JWTBearer(superuser, employee)
def get_tour_guide_by_user_id(user_id: str):
    return TourGuideController.get_tour_guide_by_user_id(user_id)


@tour_guide_router.get(
    "/get-tour-guide-by-name-or-lastname", response_model=list[TourGuideSchema]
)  # TODO Add dependencies JWTBearer(superuser, employee)
def get_tour_guide_by_name_or_last_name(name_lastname: str):
    return TourGuideController.get_tour_guide_by_name_or_last_name(name_lastname)


@tour_guide_router.put(
    "/update-tour-guide-data", response_model=TourGuideSchema
)  # TODO Add dependencies JWTBearer(superuser, employee)
def update_tour_guide_data(tour_guide: TourGuideSchemaUpdate):
    return TourGuideController.update_tour_guide_data(
        tour_guide.id, tour_guide.name, tour_guide.last_name, tour_guide.phone_number
    )


@tour_guide_router.put(
    "/update-tour-guide-language", response_model=TourGuideSchema
)  # TODO Add dependencies JWTBearer(superuser, employee)
def update_tour_guide_language(tour_guide: TourGuideSchemaLanguageUpdate):
    return TourGuideController.update_tour_guide_language(tour_guide.id, tour_guide.language_id)


@tour_guide_router.put(
    "/update-tour-guide-is_employee", response_model=TourGuideSchema
)  # TODO Add dependencies JWTBearer(superuser, employee)
def update_tour_guide_is_employee(tour_guide: TourGuideSchemaIsEmployeeUpdate):
    return TourGuideController.update_tour_guide_is_employee(tour_guide.id, tour_guide.is_employee)


@tour_guide_router.delete("/delete-tour-guide")  # TODO Add dependencies JWTBearer(superuser)
def delete_tour_guide_by_id(tour_guide_id: str):
    return TourGuideController.delete_tour_guide_by_id(tour_guide_id)


customer_router = APIRouter(prefix="/api/customers", tags=["Customers"])


@customer_router.post(
    "/add-new-customer", response_model=CustomerSchema
)  # TODO Add dependencies JWTBearer(superuser, employee)
def create_customer(customer: CustomerSchemaInput):
    return CustomerController.create_customer(
        customer.name, customer.last_name, customer.phone_number, customer.address, customer.city, customer.user_id
    )


@customer_router.get(
    "/get-all-customers", response_model=list[CustomerSchema]
)  # TODO Add dependencies JWTBearer(superuser, employee)
def get_all_customers():
    return CustomerController.get_all_customers()


@customer_router.get(
    "/get-customer-by-id", response_model=CustomerSchema
)  # TODO Add dependencies JWTBearer(superuser, employee, tour_guide)
def get_customer_by_id(customer_id: str):
    return CustomerController.get_customer_by_id(customer_id)


@customer_router.get(
    "/get-customer-by-user-id", response_model=CustomerSchema
)  # TODO Add dependencies JWTBearer(superuser, employee)
def get_customer_by_user_id(user_id: str):
    return CustomerController.get_customer_by_user_id(user_id)


@customer_router.get(
    "/get-customer-by-name-or-lastname", response_model=list[CustomerSchema]
)  # TODO Add dependencies JWTBearer(superuser, employee, tour_guide)
def get_customer_by_name_or_lastname(name_lastname: str):
    return CustomerController.get_customer_by_name_or_lastname(name_lastname)


@customer_router.post(
    "/update-customer-data", response_model=CustomerSchema
)  # TODO Add dependencies (superuser, employee)
def update_customer_data(customer: CustomerSchemaUpdate):
    return CustomerController.update_customer_data(
        customer.id, customer.name, customer.last_name, customer.phone_number, customer.address, customer.city
    )


@customer_router.delete("/delete-customer")
def delete_customer_by_id(customer_id: str):
    return CustomerController.delete_customer_by_id(customer_id)
