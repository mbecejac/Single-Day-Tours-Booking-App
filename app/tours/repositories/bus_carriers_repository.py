from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.tours.exceptions import BusCarrierExceptionCity, BusCarrierExceptionName, BusCarrierNotFoundException
from app.tours.models import BusCarrier


class BusCarrierRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_bus_carrier(self, name: str, email: str, phone_number: str, address: str, city: str):
        try:
            bus_carrier = BusCarrier(name, email, phone_number, address, city)
            self.db.add(bus_carrier)
            self.db.commit()
            self.db.refresh(bus_carrier)
            return bus_carrier
        except IntegrityError as e:
            raise e
        except Exception as e:
            raise e

    def read_all_bus_carriers(self):
        return self.db.query(BusCarrier).all()

    def read_bus_carrier_by_id(self, bus_carrier_id: str):
        bus_carrier = self.db.query(BusCarrier).filter(BusCarrier.id == bus_carrier_id).first()
        if bus_carrier is None:
            raise BusCarrierNotFoundException(
                message=f"Bus carrier with provided ID: {bus_carrier_id} not found.", code=400
            )
        return bus_carrier

    def read_bus_carrier_by_name(self, name: str):
        bus_carrier = self.db.query(BusCarrier).filter(BusCarrier.name.ilike(f"%{name}%")).first()
        if bus_carrier is None:
            raise BusCarrierExceptionName(message=f"Bus carrier with provided name: {name} not found.", code=400)
        return bus_carrier

    def read_bus_carrier_by_city(self, city: str):
        bus_carrier = self.db.query(BusCarrier).filter(BusCarrier.city.ilike(f"%{city}%")).first()
        if bus_carrier is None:
            raise BusCarrierExceptionCity(message=f"Bus carrier with provided city: {city} not found.", code=400)
        return bus_carrier

    def bus_carrier_check(self, name: str):
        bus_carrier = self.db.query(BusCarrier).filter(BusCarrier.name.ilike(f"%{name}%")).first()
        return bus_carrier

    def delete_bus_carrier_by_id(self, bus_carrier_id: str):
        try:
            bus_carrier = self.db.query(BusCarrier).filter(BusCarrier.id == bus_carrier_id).first()
            if bus_carrier is None:
                raise BusCarrierNotFoundException(
                    message=f"Bus carrier with provided ID: {bus_carrier_id} not found.", code=400
                )
            self.db.delete(bus_carrier)
            self.db.commit()
            return True
        except Exception as e:
            raise e
