from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.users.exceptions import EmployeeNotFoundException
from app.users.models import Employee


class EmployeeRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_employee(self, user_id: str):
        try:
            employee = Employee(user_id)
            self.db.add(employee)
            self.db.commit()
            self.db.refresh(employee)
            return employee
        except IntegrityError as e:
            raise e

    def read_all_employees(self):
        return self.db.query(Employee).all()

    def read_employee_by_id(self, employee_id: int):
        employee = self.db.query(Employee).filter(Employee.id == employee_id).first()
        if employee is None:
            raise EmployeeNotFoundException(message=f"Employee with provided id: {employee_id} not found", code=400)
        return employee

    def read_employee_by_user_id(self, user_id: str):
        employee = self.db.query(Employee).filter(Employee.user_id == user_id).first()
        return employee

    def delete_employee_by_id(self, employee_id: str):
        try:
            employee = self.db.query(Employee).filter(Employee.id == employee_id).first()
            if employee is None:
                raise EmployeeNotFoundException(
                    message=f"Employee with provided id: {employee_id} not found.", code=400
                )
            self.db.delete(employee)
            self.db.commit()
            return True
        except Exception as e:
            raise e
