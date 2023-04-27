import httpx 
from Todo import Todo
from TodoDAO import TodoDAO


def main():

    with TodoDAO("todos_db.db") as dao:
        for todo in dao.findAll():
            print(todo)


if __name__ == '__main__':
    main()
