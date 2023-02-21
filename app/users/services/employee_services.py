"""Employee related services"""
from app.db import SessionLocal
from app.users.exceptions import EmployeeExceptionId
from app.users.repositories import EmployeeRepository


class EmployeeService:
    """Service for employee management"""

    @staticmethod
    def create_employee(user_id: str):
        """Create a new employee"""
        try:
            with SessionLocal() as db:
                employee_repository = EmployeeRepository(db)
                employee_check = employee_repository.read_employee_by_user_id(user_id)
                if employee_check is None:
                    return employee_repository.create_employee(user_id)
                raise EmployeeExceptionId(message="User is already employee.", code=400)
        except Exception as e:
            raise e

    @staticmethod
    def read_all_employees():
        """Read all employees"""
        try:
            with SessionLocal() as db:
                employee_repository = EmployeeRepository(db)
                return employee_repository.read_all_employees()
        except Exception as e:
            raise e

    @staticmethod
    def read_employee_by_id(employee_id: int):
        """Read employee by provided id"""
        try:
            with SessionLocal() as db:
                employee_repository = EmployeeRepository(db)
                return employee_repository.read_employee_by_id(employee_id)
        except Exception as e:
            raise e

    @staticmethod
    def read_employee_by_user_id(user_id: str):
        """Read employee by provided user id"""
        try:
            with SessionLocal() as db:
                employee_repository = EmployeeRepository(db)
                return employee_repository.read_employee_by_user_id(user_id)
        except Exception as e:
            raise e

    @staticmethod
    def delete_employee_by_id(employee_id: str):
        """Delete employee by provided id"""
        try:
            with SessionLocal() as db:
                employee_repository = EmployeeRepository(db)
                return employee_repository.delete_employee_by_id(employee_id)
        except Exception as e:
            raise e
