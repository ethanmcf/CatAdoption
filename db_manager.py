import sqlite3

#table name cats

class DBManager:
    def __init__(self):
        self.conn = sqlite3.connect(('seen_cats.db'))
        self.cur = self.conn.cursor()
    
    def add_to_seen(self,name):
        self.cur.execute("INSERT INTO cats VALUES ('{}')".format(name))
        self.conn.commit()
    
    def is_seen(self,name):
        self.cur.execute("SELECT * FROM cats WHERE name= '{}'".format(name))
        query = self.cur.fetchone()
        self.conn.commit()
        if query == None:
            return False
        return True

    

    def finish(self):
        self.conn.commit()
        self.conn.close()


