class EmployeeNotFoundException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class EmployeeExceptionId(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code
