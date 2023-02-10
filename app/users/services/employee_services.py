from app.db import SessionLocal
from app.users.exceptions import EmployeeExceptionId
from app.users.repository import EmployeeRepository


class EmployeeService:
    @staticmethod
    def create_employee(user_id: str):
        try:
            with SessionLocal() as db:
                employee_repository = EmployeeRepository(db)
                employee_check = employee_repository.read_employee_by_user_id(user_id)
                if employee_check is None:
                    return employee_repository.create_employee(user_id)
                raise EmployeeExceptionId(code=400, message="User is already employee.")
        except Exception as e:
            raise e

    @staticmethod
    def read_all_employees():
        try:
            with SessionLocal() as db:
                employee_repository = EmployeeRepository(db)
                return employee_repository.read_all_employees()
        except Exception as e:
            raise e

    @staticmethod
    def read_employee_by_id(employee_id: int):
        try:
            with SessionLocal() as db:
                employee_repository = EmployeeRepository(db)
                return employee_repository.read_employee_by_id(employee_id)
        except Exception as e:
            raise e

    @staticmethod
    def read_employee_by_user_id(user_id: str):
        try:
            with SessionLocal() as db:
                employee_repository = EmployeeRepository(db)
                return employee_repository.read_employee_by_user_id(user_id)
        except Exception as e:
            raise e

    @staticmethod
    def delete_employee_by_id(employee_id: str):
        try:
            with SessionLocal() as db:
                employee_repository = EmployeeRepository(db)
                return employee_repository.delete_employee_by_id(employee_id)
        except Exception as e:
            raise e
