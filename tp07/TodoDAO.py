from Todo import Todo
import sqlite3

class TodoDAO:

    def __init__(self,db_file):
        self.__con = sqlite3.connect(db_file)

    def save(self,todo:Todo)->None:
        """
        save the todo
        """
        cur = self.__con.cursor()
        sql = f"""INSERT INTO todos_tbl(user_id,title,completed)
VALUES({todo.userId},'{todo.title}',{todo.completed})        
        """
        cur.execute(sql)
        self.__con.commit()

    def findAll(self)->list[Todo]:
        pass

    def __del__(self):
        self.__con.close()