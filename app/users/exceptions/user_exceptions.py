"""User related exceptions"""


class UserNotFoundException(Exception):
    """Exception raised when a user is not found."""

    def __init__(self, message, code):
        self.message = message
        self.code = code


class UserInvalidPassword(Exception):
    """Exception raised when an invalid password is provided."""

    def __init__(self, message, code):
        self.message = message
        self.code = code
