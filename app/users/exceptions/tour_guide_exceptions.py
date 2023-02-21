"""Tour guide related exceptions"""


class TourGuideNotFoundException(Exception):
    """Exception raised when a tour guide is not found."""

    def __init__(self, message, code):
        self.message = message
        self.code = code


class TourGuideExceptionName(Exception):
    """Exception raised when an invalid tour guide name or lastname is provided."""

    def __init__(self, message, code):
        self.message = message
        self.code = code


class TourGuideExistsException(Exception):
    """Exception raised when tour guide already exists"""

    def __init__(self, message, code):
        self.message = message
        self.code = code
