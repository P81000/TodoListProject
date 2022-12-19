class NoTodoListError(Exception):
    def __init__(self):
        message = "No todo list."
        super().__init__(message)