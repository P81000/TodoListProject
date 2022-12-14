from src.usecases.errors.invalidusererror import InvalidUserError
from src.usecases.errors.notodolisterror import NoTodoListError

class RemoveTodoList:
    def __init__(self, todolist_repo, user_repo):
        self.todolist_repo = todolist_repo
        self.user_repo = user_repo

    def perform(self, user_email):
        todolist = self.todolist_repo.find_by_email(user_email)
        user = self.user_repo.find_by_email(user_email)
        if not user:
            raise InvalidUserError()
        if user and not todolist:
            raise NoTodoListError()
        self.todolist_repo.delete(user_email)