from app.db import SessionLocal
from app.users.repository import CustomerRepository


class CustomerService:
    @staticmethod
    def create_customer(name: str, last_name: str, phone_number: str, address: str, city: str, user_id: str):
        try:
            with SessionLocal() as db:
                customer_repository = CustomerRepository(db)
                return customer_repository.create_customer(name, last_name, phone_number, address, city, user_id)
        except Exception as e:
            raise e

    @staticmethod
    def read_customer_by_id(customer_id: str):
        try:
            with SessionLocal() as db:
                customer_repository = CustomerRepository(db)
                return customer_repository.read_customer_by_id(customer_id)
        except Exception as e:
            raise e

    @staticmethod
    def read_customer_by_user_id(user_id: str):
        try:
            with SessionLocal() as db:
                customer_repository = CustomerRepository(db)
                return customer_repository.read_customer_by_user_id(user_id)
        except Exception as e:
            raise e

    @staticmethod
    def read_customer_by_name_or_last_name(name_lastname: str):
        try:
            with SessionLocal() as db:
                customer_repository = CustomerRepository(db)
                return customer_repository.read_customer_by_name_or_lastname(name_lastname)
        except Exception as e:
            raise e

    @staticmethod
    def update_customer_data(
        customer_id: str,
        name: str = None,
        last_name: str = None,
        phone_number: str = None,
        address: str = None,
        city: str = None,
    ):
        try:
            with SessionLocal() as db:
                customer_repository = CustomerRepository(db)
                return customer_repository.update_customer_data(
                    customer_id, name, last_name, phone_number, address, city
                )
        except Exception as e:
            raise e

    @staticmethod
    def delete_customer_by_id(customer_id: str):
        try:
            with SessionLocal() as db:
                customer_repository = CustomerRepository(db)
                return customer_repository.delete_customer_by_id(customer_id)
        except Exception as e:
            raise e
