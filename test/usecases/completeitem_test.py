from test.usecases.inmemoryuserrepository import InMemoryUserRepository
from test.usecases.inmemorytodolistrepository import InMemoryTodoListRepository
from test.usecases.fakehashservice import FakeHashService
from src.usecases.createtodolist import CreateTodoList
from src.usecases.createtodoitem import CreateTodoItem
from src.usecases.signup import SignUp
from src.usecases.createtodolist import TodoList
from src.usecases.createtodoitem import TodoItem
from src.usecases.completetodoitem import CompleteTodoItem
from src.usecases.errors.invalidusererror import InvalidUserError
import pytest

def test_complete_item_in_todo_list():
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
    usecase = CompleteTodoItem(todolist_repo)
    usecase.perform(user_email, item_description)
    persisted_todo_list = todolist_repo.find_by_email(user_email)
    assert persisted_todo_list.get(0).description == item_description
    assert persisted_todo_list.get(0).complete

def test_complete_item_invalid_user():
    user_repo = InMemoryUserRepository()
    todolist_repo = InMemoryTodoListRepository()
    user_email = 'invalid@user.com'
    user_password = 'test1234TEST&'
    item_description = 'call mom'
    usecase = CompleteTodoItem(todolist_repo)
    with pytest.raises(InvalidUserError):
        usecase.perform(user_email, item_description)

