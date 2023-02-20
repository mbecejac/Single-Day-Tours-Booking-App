from fastapi import HTTPException, Response

from app.tours.exceptions import BusCarrierExceptionCity, BusCarrierExceptionName, BusCarrierNotFoundException
from app.tours.services import BusCarrierService


class BusCarrierController:
    @staticmethod
    def create_bus_carrier(name: str, email: str, phone_number: str, address: str, city: str):
        try:
            bus_carrier = BusCarrierService.create_bus_carrier(name, email, phone_number, address, city)
            return bus_carrier
        except BusCarrierExceptionName as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_all_bus_carriers():
        return BusCarrierService.read_all_bus_carriers()

    @staticmethod
    def get_bus_carrier_by_id(bus_carrier_id: str):
        try:
            bus_carrier = BusCarrierService.read_bus_carrier_by_id(bus_carrier_id)
            return bus_carrier
        except BusCarrierNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_bus_carrier_by_name(name: str):
        try:
            bus_carrier = BusCarrierService.read_bus_carrier_by_name(name)
            return bus_carrier
        except BusCarrierExceptionName as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_bus_carrier_by_city(city: str):
        try:
            bus_carrier = BusCarrierService.read_bus_carrier_by_city(city)
            return bus_carrier
        except BusCarrierExceptionCity as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def delete_bus_carrier_by_id(bus_carrier_id: str):
        try:
            if BusCarrierService.delete_bus_carrier_by_id(bus_carrier_id):
                return Response(content=f"Bus carrier with ID: {bus_carrier_id} deleted.", status_code=200)
        except BusCarrierNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
