from test.usecases.inmemoryuserrepository import InMemoryUserRepository
from test.usecases.inmemorytodolistrepository import InMemoryTodoListRepository
from test.usecases.fakehashservice import FakeHashService
from src.usecases.createtodolist import CreateTodoList
from src.usecases.createtodoitem import CreateTodoItem
from src.usecases.signup import SignUp
from src.usecases.removetodolist import RemoveTodoList
from src.usecases.errors.invalidusererror import InvalidUserError
from src.usecases.createtodolist import TodoList
from src.usecases.createtodoitem import TodoItem
import pytest

def test_remove_todo_list():
    user_repo = InMemoryUserRepository()
    todolist_repo = InMemoryTodoListRepository()
    hash_service = FakeHashService()
    user_name = 'Joe Doe'
    user_email = 'joe@doe.com'
    user_password = 'test1234TEST&'
    item_description = 'call mom'
    item_priority = 0
    SignUp(user_repo, hash_service).perform(user_name, user_email, user_password)
    CreateTodoList(user_repo, todolist_repo).perform(user_email)
    CreateTodoItem(todolist_repo).perform(user_email, item_description, item_priority)
    usecase = RemoveTodoList(todolist_repo, user_repo)
    usecase.perform(user_email)
    persisted_todo_list = todolist_repo.find_by_email(user_email)
    assert persisted_todo_list is None

def test_remove_todo_list_with_invalid_user():
    user_repo = InMemoryUserRepository()
    todolist_repo = InMemoryTodoListRepository()
    user_email = 'invalid@email.com'
    usecase = RemoveTodoList(todolist_repo, user_repo)
    with pytest.raises(InvalidUserError):
        usecase.perform(user_email)
