from Todo import Todo
import sqlite3

class TodoDAO:

    def __init__(self,db_file):
        self.__con = sqlite3.connect(db_file)
    
    def __enter__(self):
        print("def __enter__(self)")
        return self
    
    def __exit__(self, *exc):
        print("def __exit__(self, *exc):")
        self.__con.close()
    

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

    # def findAll(self)->list[Todo]:
    #     r = []
    #     cur = self.__con.cursor()
    #     sql = "SELECT id,user_id,title,completed FROM todos_tbl"
    #     res = cur.execute(sql)
        
    #     for id,user_id,title,completed in res.fetchall():
    #         t = Todo(id,user_id,title,completed)
    #         r.append(t)

    #     return r
    
    def findAll(self):
        cur = self.__con.cursor()
        sql = "SELECT id,user_id,title,completed FROM todos_tbl"
        res = cur.execute(sql)
        
        for id,user_id,title,completed in res.fetchall():
            t = Todo(id,user_id,title,completed)
            yield t


    def __del__(self):
        self.__con.close()