import pytest
from sqlalchemy.exc import IntegrityError

from app.tests import TestClass, TestingSessionLocal
from app.tours.exceptions import BusCarrierExceptionCity, BusCarrierExceptionName, BusCarrierNotFoundException
from app.tours.repositories import BusCarrierRepository


class TestBusCarrierRepository(TestClass):
    def test_create_bus_carrier(self):
        with TestingSessionLocal() as db:
            bus_carrier_repo = BusCarrierRepository(db)
            bus_carrier = bus_carrier_repo.create_bus_carrier(
                "Test1", "test_bus@test.te", "+38166658995", "Testing Street 342", "Test City"
            )
            assert bus_carrier.name == "Test1"
            assert bus_carrier.email == "test_bus@test.te"
            assert bus_carrier.phone_number == "+38166658995"
            assert bus_carrier.address == "Testing Street 342"
            assert bus_carrier.city == "Test City"

    def test_create_bus_carrier_error(self):
        with TestingSessionLocal() as db:
            bus_carrier_repo = BusCarrierRepository(db)
            bus_carrier = bus_carrier_repo.create_bus_carrier(
                "Test1", "test_bus@test.te", "+38166658995", "Testing Street 342", "Test City"
            )
            assert bus_carrier.name == "Test1"
            with pytest.raises(IntegrityError):
                bus_carrier_repo.create_bus_carrier(
                    "Test1", "test_bus@test.te", "+38166658995", "Testing Street 342", "Test City"
                )

    def test_read_all_bus_carriers_if_none(self):
        with TestingSessionLocal() as db:
            bus_carrier_repository = BusCarrierRepository(db)
            all_bus_carriers = bus_carrier_repository.read_all_bus_carriers()
            assert all_bus_carriers == []

    def test_read_all_bus_carriers(self):
        with TestingSessionLocal() as db:
            bus_carrier_repository = BusCarrierRepository(db)
            bus_carrier_repository.create_bus_carrier(
                "Test1", "test_bus@test.te", "+38166658995", "Testing Street 342", "Test City"
            )
            bus_carrier_repository.create_bus_carrier(
                "Test2", "test_bus2@test.te", "+38166658995", "Testing Street 342", "Test City"
            )
            all_bus_carriers = bus_carrier_repository.read_all_bus_carriers()
            assert len(all_bus_carriers) == 2

    def test_read_all_bus_carriers_error(self):
        with TestingSessionLocal() as db:
            bus_carrier_repository = BusCarrierRepository(db)
            bus_carrier_repository.create_bus_carrier(
                "Test1", "test_bus@test.te", "+38166658995", "Testing Street 342", "Test City"
            )
            bus_carrier_repository.create_bus_carrier(
                "Test2", "test_bus2@test.te", "+38166658995", "Testing Street 342", "Test City"
            )
            all_bus_carriers = bus_carrier_repository.read_all_bus_carriers()
            assert not len(all_bus_carriers) != 2

    def test_read_bus_carrier_by_id(self):
        with TestingSessionLocal() as db:
            bus_carrier_repository = BusCarrierRepository(db)
            bus_carrier = bus_carrier_repository.create_bus_carrier(
                "Test1", "test_bus@test.te", "+38166658995", "Testing Street 342", "Test City"
            )
            bus_carrier1 = bus_carrier_repository.read_bus_carrier_by_id(bus_carrier.id)
            assert bus_carrier1 is not None
            with pytest.raises(BusCarrierNotFoundException):
                bus_carrier_repository.read_bus_carrier_by_id("false_id")

    def test_read_bus_carrier_by_name(self):
        with TestingSessionLocal() as db:
            bus_carrier_repository = BusCarrierRepository(db)
            bus_carrier = bus_carrier_repository.create_bus_carrier(
                "Test1", "test_bus@test.te", "+38166658995", "Testing Street 342", "Test City"
            )
            assert bus_carrier is not None
            bus_carrier1 = bus_carrier_repository.read_bus_carrier_by_name(bus_carrier.name)
            assert bus_carrier1.name == bus_carrier.name
            assert bus_carrier1 is not None
            with pytest.raises(BusCarrierExceptionName):
                bus_carrier_repository.read_bus_carrier_by_name("No Name")

    def test_read_bus_carrier_by_city(self):
        with TestingSessionLocal() as db:
            bus_carrier_repository = BusCarrierRepository(db)
            bus_carrier = bus_carrier_repository.create_bus_carrier(
                "Test1", "test_bus@test.te", "+38166658995", "Testing Street 342", "Test City"
            )
            assert bus_carrier is not None
            bus_carrier1 = bus_carrier_repository.read_bus_carrier_by_city(bus_carrier.city)
            assert bus_carrier1.city == bus_carrier.city
            assert bus_carrier1 is not None
            with pytest.raises(BusCarrierExceptionCity):
                bus_carrier_repository.read_bus_carrier_by_city("No Name")

    def test_delete_bus_carrier_by_id(self):
        with TestingSessionLocal() as db:
            bus_carrier_repository = BusCarrierRepository(db)
            bus_carrier = bus_carrier_repository.create_bus_carrier(
                "Test1", "test_bus@test.te", "+38166658995", "Testing Street 342", "Test City"
            )
            assert bus_carrier is not None
            with pytest.raises(BusCarrierNotFoundException):
                bus_carrier_repository.read_bus_carrier_by_id("false_id")
            bus_carrier_delete = bus_carrier_repository.delete_bus_carrier_by_id(bus_carrier.id)
            assert bus_carrier_delete is True
