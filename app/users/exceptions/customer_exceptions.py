class CustomerNotFoundException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class CustomerExceptionName(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class CustomerExistsException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code
