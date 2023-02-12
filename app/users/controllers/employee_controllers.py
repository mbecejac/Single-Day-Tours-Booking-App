from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError

from app.users.exceptions import EmployeeNotFoundException
from app.users.services import EmployeeService


class EmployeeController:
    @staticmethod
    def create_employee(user_id: str):
        try:
            employee = EmployeeService.create_employee(user_id)
            return employee
        except IntegrityError:
            raise HTTPException(status_code=400, detail=f"Employee with user id: {user_id}, already exist.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_all_employees():
        return EmployeeService.read_all_employees()

    @staticmethod
    def get_employee_by_id(employee_id: int):
        try:
            employee = EmployeeService.read_employee_by_id(employee_id)
            return employee
        except EmployeeNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_employee_by_user_id(user_id: str):
        try:
            employee = EmployeeService.read_employee_by_user_id(user_id)
            return employee
        except EmployeeNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def delete_employee_by_id(employee_id: str):
        try:
            EmployeeService.delete_employee_by_id(employee_id)
            return {"message": f"Employee with id: {employee_id} is deleted"}
        except EmployeeNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
