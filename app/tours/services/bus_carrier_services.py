from app.db import SessionLocal
from app.tours.exceptions import BusCarrierExceptionName
from app.tours.repositories import BusCarrierRepository


class BusCarrierService:
    @staticmethod
    def create_bus_carrier(name: str, email: str, phone_number: str, address: str, city: str):
        try:
            with SessionLocal() as db:
                bus_carrier_repository = BusCarrierRepository(db)
                bus_carrier_check = bus_carrier_repository.read_bus_carrier_by_name(name)
                if bus_carrier_check is False:
                    return bus_carrier_repository.create_bus_carrier(name, email, phone_number, address, city)
                raise BusCarrierExceptionName(
                    message=f"Bus carrier with name {name} already exists in database.", code=400
                )
        except Exception as e:
            raise e

    @staticmethod
    def read_all_bus_carriers():
        try:
            with SessionLocal() as db:
                bus_carrier_repository = BusCarrierRepository(db)
                return bus_carrier_repository.read_all_bus_carriers()
        except Exception as e:
            raise e

    @staticmethod
    def read_bus_carrier_by_id(bus_carrier_id: str):
        try:
            with SessionLocal() as db:
                bus_carrier_repository = BusCarrierRepository(db)
                return bus_carrier_repository.read_bus_carrier_by_id(bus_carrier_id)
        except Exception as e:
            raise e

    @staticmethod
    def read_bus_carrier_by_name(name: str):
        try:
            with SessionLocal() as db:
                bus_carrier_repository = BusCarrierRepository(db)
                return bus_carrier_repository.read_bus_carrier_by_name(name)
        except Exception as e:
            raise e

    @staticmethod
    def read_bus_carrier_by_city(city: str):
        try:
            with SessionLocal() as db:
                bus_carrier_repository = BusCarrierRepository(db)
                return bus_carrier_repository.read_bus_carrier_by_city(city)
        except Exception as e:
            raise e

    @staticmethod
    def delete_bus_carrier_by_id(bus_carrier_id: str):
        try:
            with SessionLocal() as db:
                bus_carrier_repository = BusCarrierRepository(db)
                return bus_carrier_repository.delete_bus_carrier_by_id(bus_carrier_id)
        except Exception as e:
            raise e
