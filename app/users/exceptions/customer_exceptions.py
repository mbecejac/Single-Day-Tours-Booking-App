"""Customer related exceptions"""


class CustomerNotFoundException(Exception):
    """Exception raised when a customer is not found."""

    def __init__(self, message, code):
        self.message = message
        self.code = code


class CustomerExceptionName(Exception):
    """Exception raised when an invalid customer name or lastname is provided."""

    def __init__(self, message, code):
        self.message = message
        self.code = code


class CustomerExistsException(Exception):
    """Exception raised when provided user id is already used to create customer."""

    def __init__(self, message, code):
        self.message = message
        self.code = code
