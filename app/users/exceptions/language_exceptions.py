"""Language related exceptions"""


class LanguageNotFoundException(Exception):
    """Exception raised when a language is not found."""

    def __init__(self, message, code):
        self.message = message
        self.code = code


class LanguageExceptionName(Exception):
    """Exception raised when an invalid language name is provided."""

    def __init__(self, message, code):
        self.message = message
        self.code = code
