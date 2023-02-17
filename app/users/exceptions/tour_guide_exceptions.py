class TourGuideNotFoundException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class TourGuideExceptionName(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class TourGuideExistsException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code
