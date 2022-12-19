class InvalidPasswordError(Exception):
  def __init__(self):
    message = "Invalid Password."
    super().__init__(message)