from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.users.exceptions import CustomerExceptionName, CustomerNotFoundException
from app.users.models import Customer


class CustomerRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_customer(self, name: str, last_name: str, phone_number: str, address: str, city: str, user_id: str):
        try:
            customer = Customer(name, last_name, phone_number, address, city, user_id)
            self.db.add(customer)
            self.db.commit()
            self.db.refresh(customer)
            return customer
        except IntegrityError as e:
            raise e

    def read_customer_by_id(self, customer_id: str):
        customer = self.db.query(Customer).filter(Customer.id == customer_id).first()
        if customer is None:
            raise CustomerNotFoundException(message=f"Customer with provided id: {customer_id} not found", code=400)
        return customer

    def read_customer_by_user_id(self, user_id: str):
        customer = self.db.query(Customer).filter(Customer.user_id == user_id).first()
        if customer is None:
            raise CustomerNotFoundException(message=f"Customer with provided user id: {user_id} not found", code=400)
        return customer

    def read_customer_by_name_or_lastname(self, name_lastname: str):
        try:
            customers = (
                self.db.query(Customer).filter(Customer.name.ilike(f"%{name_lastname}%")).all()
                or self.db.query(Customer).filter(Customer.last_name.ilike(f"%{name_lastname}%")).all()
            )
            if customers is None:
                raise CustomerExceptionName(
                    message=f"Customer with provided name or last name: {name_lastname} not found", code=400
                )
            return customers
        except Exception as e:
            raise e

    def update_customer_data(
        self,
        customer_id: str,
        name: str = None,
        last_name: str = None,
        phone_number: str = None,
        address: str = None,
        city: str = None,
    ):
        try:
            customer = self.db.query(Customer).filter(Customer.id == customer_id).first()
            if customer is None:
                raise CustomerNotFoundException(message=f"Customer with provided id: {customer_id} not found", code=400)
            if name is not None:
                customer.name = name
            if last_name is not None:
                customer.last_name = last_name
            if phone_number is not None:
                customer.phone_number = phone_number
            if address is not None:
                customer.address = address
            if city is not None:
                customer.city = city
            self.db.add(customer)
            self.db.commit()
            self.db.refresh(customer)
            return customer
        except Exception as e:
            raise e

    def delete_customer_by_id(self, customer_id: str):
        try:
            customer = self.db.query(Customer).filter(Customer.id == customer_id).first()
            if customer is None:
                raise CustomerNotFoundException(message=f"Customer with provided id: {customer_id} not found", code=400)
            self.db.delete(customer)
            self.db.commit()
            return True
        except Exception as e:
            raise e
