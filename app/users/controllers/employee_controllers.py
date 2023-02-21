"""Employee related controllers"""
from fastapi import HTTPException

from app.users.exceptions import EmployeeExceptionId, EmployeeNotFoundException
from app.users.services import EmployeeService


class EmployeeController:
    """Controller for employee management"""

    @staticmethod
    def create_employee(user_id: str):
        """Create a new employee"""
        try:
            employee = EmployeeService.create_employee(user_id)
            return employee
        except EmployeeExceptionId:
            raise HTTPException(status_code=400, detail=f"Employee with user id: {user_id}, already exist.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_all_employees():
        """Get all employees"""
        return EmployeeService.read_all_employees()

    @staticmethod
    def get_employee_by_id(employee_id: int):
        """Get employee by provided employee id"""
        try:
            employee = EmployeeService.read_employee_by_id(employee_id)
            return employee
        except EmployeeNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_employee_by_user_id(user_id: str):
        """Get employee by provided user id"""
        try:
            employee = EmployeeService.read_employee_by_user_id(user_id)
            return employee
        except EmployeeNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def delete_employee_by_id(employee_id: str):
        """Delete employee by provided employee id"""
        try:
            EmployeeService.delete_employee_by_id(employee_id)
            return {"message": f"Employee with id: {employee_id} is deleted"}
        except EmployeeNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
