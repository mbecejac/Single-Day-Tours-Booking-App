class TourNotFoundException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class TourExceptionName(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class TourExceptionDate(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class TourExceptionLocation(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class TourExceptionPrice(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class TourExceptionWalkingTour(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class TourExceptionLanguage(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class TourExceptionActive(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code
