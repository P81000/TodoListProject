class DuplicateItemError(Exception):
    def __init__(self):
        message = "Duplicate Item."
        super().__init__(message)