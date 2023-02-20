from fastapi import APIRouter

from app.tours.controllers import BusCarrierController, TourApplicationController, TourController
from app.tours.schemas import (
    BusCarrierSchema,
    BusCarrierSchemaInput,
    TourApplicationSchema,
    TourApplicationSchemaInput,
    TourSchema,
    TourSchemaInput,
)

bus_carrier_router = APIRouter(prefix="/api/bus-carriers", tags=["Bus Carriers"])


@bus_carrier_router.post(
    "/add-new-bus-carrier", response_model=BusCarrierSchema
)  # TODO Add dependencies JWTBearer(superuser, employee)
def create_bus_carrier(bus_carrier: BusCarrierSchemaInput):
    return BusCarrierController.create_bus_carrier(
        name=bus_carrier.name,
        email=bus_carrier.email,
        phone_number=bus_carrier.phone_number,
        address=bus_carrier.address,
        city=bus_carrier.city,
    )


@bus_carrier_router.get(
    "/get-all-bus_carriers", response_model=list[BusCarrierSchema]
)  # TODO Add dependencies JWTBearer(superuser, employee)
def get_all_bus_carriers():
    return BusCarrierController.get_all_bus_carriers()


@bus_carrier_router.get(
    "/get-bus-carrier-by-id", response_model=BusCarrierSchema
)  # TODO Add dependencies JWTBearer(superuser, employee)
def get_bus_carrier_by_id(bus_carrier_id: str):
    return BusCarrierController.get_bus_carrier_by_id(bus_carrier_id)


@bus_carrier_router.get(
    "/get-bus-carrier-by-name", response_model=BusCarrierSchema
)  # TODO Add dependencies JWTBearer(superuser, employee)
def get_bus_carrier_by_name(name: str):
    return BusCarrierController.get_bus_carrier_by_name(name)


@bus_carrier_router.get(
    "/get-bus-carrier-by-city", response_model=BusCarrierSchema
)  # TODO Add dependencies JWTBearer(superuser, employee)
def get_bus_carrier_by_city(city: str):
    return BusCarrierController.get_bus_carrier_by_city(city)


@bus_carrier_router.delete("/delete-bus-carrier")  # TODO Add dependencies JWTBearer(superuser)
def delete_bus_carrier_by_id(bus_carrier_id: str):
    return BusCarrierController.delete_bus_carrier_by_id(bus_carrier_id)


tour_router = APIRouter(prefix="/api/tours", tags=["Tours"])


@tour_router.post("/add-new-tour", response_model=TourSchema)  # TODO Add dependencies JWTBearer(superuser, employee)
def create_tour(tour: TourSchemaInput):
    return TourController.create_tour(
        tour_name=tour.tour_name,
        tour_date=tour.tour_date,
        location=tour.location,
        description=tour.description,
        price=tour.price,
        is_walking_tour=tour.is_walking_tour,
        tour_language=tour.tour_language,
        tour_guide_id=tour.tour_guide_id,
    )


@tour_router.get("/get-all-tours", response_model=list[TourSchema])
def get_all_tours():
    return TourController.get_all_tours()


@tour_router.get("/get-tour-by-id", response_model=TourSchema)
def get_tour_by_id(tour_id: str):
    return TourController.get_tour_by_id(tour_id)


@tour_router.get("/get-tours-by-date", response_model=list[TourSchema])
def get_tours_by_date(date: str):
    return TourController.get_tours_by_date(date)


@tour_router.get("/get-tours-by-location", response_model=list[TourSchema])
def get_tours_by_location(location: str):
    return TourController.get_tours_by_location(location)


@tour_router.get("/get-tours-by-max-price", response_model=list[TourSchema])
def get_tours_by_max_price(price: float):
    return TourController.get_tours_by_max_price(price)


@tour_router.get("/get-walking-tours", response_model=list[TourSchema])
def get_walking_tours():
    return TourController.get_walking_tours()


@tour_router.get("/get-tours-by-language", response_model=list[TourSchema])
def get_tours_by_tour_language(language: str):
    return TourController.get_tours_by_tour_language(language)


@tour_router.get("/get-active-tours", response_model=list[TourSchema])
def get_active_tours():
    return TourController.get_active_tours()


@tour_router.get("/get-active-tours-by-tour-parameters", response_model=list[TourSchema])
def get_active_tours_by_tour_parameters(tour_date: str, location: str, language: str, price: float):
    return TourController.get_active_tours_by_date_location_language_and_price(tour_date, location, language, price)


@tour_router.get(
    "/get-tour-by-tour-guide-id", response_model=list[TourSchema]
)  # TODO Add dependencies JWTBearer(superuser, employee)
def get_tour_by_tour_guide_id(tour_guide_id: str):
    return TourController.get_tour_by_tour_guide_id(tour_guide_id)


@tour_router.put(
    "/update-tour-guide-on-tour", response_model=TourSchema
)  # TODO Add dependencies JWTBearer(superuser, employee)
def update_tour_guide_on_tour(tour_id: str, tour_guide_id: str):
    return TourController.update_tour_guide_on_tour(tour_id, tour_guide_id)


@tour_router.put(
    "/update-bus-carrier-on-tour", response_model=TourSchema
)  # TODO Add dependencies JWTBearer(superuser, employee)
def update_bus_carrier_on_tour(tour_id: str, bus_carrier_id: str):
    return TourController.update_bus_carrier_on_tour(tour_id, bus_carrier_id)


@tour_router.put(
    "/update-tour-is-active", response_model=TourSchema
)  # TODO Add dependencies JWTBearer(superuser, employee)
def update_tour_is_active(tour_id: str, is_active: bool):
    return TourController.update_tour_is_active(tour_id, is_active)


@tour_router.delete("/delete-tour-by-id")  # TODO Add dependencies JWTBearer(superuser, employee)
def delete_tour_by_id(tour_id: str):
    return TourController.delete_tour_by_id(tour_id)


tour_application_router = APIRouter(prefix="/api/tour-applications", tags=["Tour Applications"])


@tour_application_router.post(
    "/add-new-tour-application", response_model=TourApplicationSchema
)  # TODO Add dependencies JWTBearer(superuser, employee)
def create_new_tour_application(tour_application: TourApplicationSchemaInput):
    return TourApplicationController.create_tour_application(
        customer_id=tour_application.customer_id, tour_id=tour_application.tour_id
    )


@tour_application_router.get(
    "/get-all-tour-applications", response_model=list[TourApplicationSchema]
)  # TODO Add dependencies JWTBearer(superuser, employee)
def get_all_tour_applications():
    return TourApplicationController.get_all_tour_applications()


@tour_application_router.get(
    "/get-tour-applications-by-id", response_model=TourApplicationSchema
)  # TODO Add dependencies JWTBearer(superuser, employee)
def get_tour_application_by_id(tour_app_id: str):
    return TourApplicationController.get_tour_application_by_id(tour_app_id)


@tour_application_router.get(
    "/get-all-active-tour-applications", response_model=list[TourApplicationSchema]
)  # TODO Add dependencies JWTBearer(superuser, employee)
def get_all_active_tour_applications():
    return TourApplicationController.get_all_active_tour_applications()


@tour_application_router.get(
    "/get-all-tour-applications-by-customer-id", response_model=list[TourApplicationSchema]
)  # TODO Add dependencies JWTBearer(superuser, employee)
def get_all_tour_applications_by_customer_id(customer_id: str):
    return TourApplicationController.get_all_tour_applications_by_customer_id(customer_id)


@tour_application_router.get(
    "/get-all-tour-applications-by-tour-id", response_model=list[TourApplicationSchema]
)  # TODO Add dependencies JWTBearer(superuser, employee, tour_guide)
def get_all_tour_applications_by_tour_id(tour_id: str):
    return TourApplicationController.get_all_tour_applications_by_tour_id(tour_id)


@tour_application_router.get(
    "/get-not-payed-tour-applications", response_model=list[TourApplicationSchema]
)  # TODO Add dependencies JWTBearer(superuser, employee)
def get_not_payed_tour_applications():
    return TourApplicationController.get_not_payed_active_tour_applications()


@tour_application_router.put(
    "/update-tour-application-is-payed", response_model=TourApplicationSchema
)  # TODO Add dependencies JWTBearer(superuser, employee)
def update_tour_application_is_payed_status(tour_app_id: str, is_payed: bool):
    return TourApplicationController.update_tour_application_is_payed_status(tour_app_id, is_payed)


@tour_application_router.put(
    "/update-tour-application-is-active", response_model=TourApplicationSchema
)  # TODO Add dependencies JWTBearer(superuser, employee)
def update_tour_application_is_active_status(tour_app_id: str, is_active: bool):
    return TourApplicationController.update_tour_application_is_active_status(tour_app_id, is_active)


@tour_application_router.put(
    "/change-custome-on-tour-application", response_model=TourApplicationSchema
)  # TODO Add dependencies JWTBearer(superuser, employee)
def change_customer_on_tour_application(tour_app_id: str, customer_id: str):
    return TourApplicationController.change_customer_on_tour_application(tour_app_id, customer_id)


@tour_application_router.delete("/delete-tour-application")  # TODO Add dependencies JWTBearer(superuser)
def delete_tour_application_by_id(tour_app_id: str):
    return TourApplicationController.delete_tour_application_by_id(tour_app_id)
