from flask import Flask,render_template
from Todo import Todo
from TodoDAO import TodoDAO

app = Flask(__name__)

@app.route("/hello")
def hello_world():
    return render_template("hello_world.html",name="Fred")


@app.route("/todos")
def todos():
    with TodoDAO("todos_db.db") as dao:
        todos = list(dao.findAll())
    
    return render_template("todos.html",all_todos=todos)
