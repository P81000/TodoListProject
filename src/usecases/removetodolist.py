
class RemoveTodoList:
    def __init__(self, todolist_repo):
        self.todolist_repo = todolist_repo

    def perform(self, user_email):
        todolist = self.todolist_repo.find_by_email(user_email)
        self.todolist_repo.delete(user_email)