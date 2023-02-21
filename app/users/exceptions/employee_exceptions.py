"""Employee related exceptions"""


class EmployeeNotFoundException(Exception):
    """Exception raised when an employee is not found."""

    def __init__(self, message, code):
        self.message = message
        self.code = code


class EmployeeExceptionId(Exception):
    """Exception raised when provided user id is already used."""

    def __init__(self, message, code):
        self.message = message
        self.code = code
