class BusCarrierNotFoundException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class BusCarrierExceptionName(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class BusCarrierExceptionCity(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class BusCarrierExistsException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code
