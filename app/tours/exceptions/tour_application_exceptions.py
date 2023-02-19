class TourApplicationNotFoundException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class TourApplicationExceptionCustomer(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class TourApplicationExceptionActive(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code
