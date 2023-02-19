from fastapi import APIRouter

from app.tours.controllers import BusCarrierController
from app.tours.schemas import BusCarrierSchema, BusCarrierSchemaInput

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
