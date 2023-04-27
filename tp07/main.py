import httpx
from Todo import Todo
from TodoDAO import TodoDAO

def main():
    r = httpx.get("https://jsonplaceholder.typicode.com/todos")
    todos = r.json()

    dao = TodoDAO("todos_db.db")
    for todo in todos:
        t = Todo(**todo)
        dao.save(t)
        print(t.title)



if __name__ == '__main__':
    main()
