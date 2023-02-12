class LanguageNotFoundException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class LanguageExceptionName(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code
