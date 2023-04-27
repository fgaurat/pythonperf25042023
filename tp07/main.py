import httpx 
from Todo import Todo
from TodoDAO import TodoDAO

def completed_todos(todos):
    for todo in todos:
        if todo.completed:
            yield todo


def main():
    dao = TodoDAO("todos_db.db")
    todos = dao.findAll()
    # t = next(todos)
    # print(t)
    # t = next(todos)
    # print(t)

    # dao.findAll() | completed_todos
    for todo in completed_todos(dao.findAll()):
        print(todo)


def main01():
    r = httpx.get("https://jsonplaceholder.typicode.com/todos")
    todos = r.json()

    dao = TodoDAO("todos_db.db")
    for todo in todos:
        t = Todo(**todo)
        dao.save(t)
        print(t.title)



if __name__ == '__main__':
    main()
