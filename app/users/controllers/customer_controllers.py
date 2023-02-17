from fastapi import HTTPException, Response

from app.users.exceptions import CustomerExistsException, CustomerNotFoundException
from app.users.services import CustomerService


class CustomerController:
    @staticmethod
    def create_customer(name: str, last_name: str, phone_number: str, address: str, city: str, user_id: str):
        try:
            customer = CustomerService.create_customer(name, last_name, phone_number, address, city, user_id)
            return customer
        except CustomerExistsException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_customer_by_id(customer_id: str):
        try:
            customer = CustomerService.read_customer_by_id(customer_id)
            return customer
        except CustomerNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_customer_by_user_id(user_id: str):
        try:
            customer = CustomerService.read_customer_by_user_id(user_id)
            return customer
        except CustomerNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_customer_by_name_or_lastname(name_lastname: str):
        try:
            customer = CustomerService.read_customer_by_name_or_last_name(name_lastname)
            return customer
        except CustomerNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

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
            customer = CustomerService.update_customer_data(customer_id, name, last_name, phone_number, address, city)
            return customer
        except CustomerNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def delete_customer_by_id(customer_id: str):
        try:
            if CustomerService.delete_customer_by_id(customer_id):
                return Response(content=f"Customer with ID: {customer_id} deleted.", status_code=200)
        except CustomerNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
