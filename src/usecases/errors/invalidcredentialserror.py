class InvalidCredentialsError(Exception):
  def __init__(self):
    message = "Invalid Credentials."
    super().__init__(message)