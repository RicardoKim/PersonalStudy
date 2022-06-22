import pymysql
from threading import RLock

class Database():
    def __init__(self):
        self.LOCK = RLock()
        self.db = pymysql.connect(host='',
                                  user='',
                                  db='',
                                  password='')
        
        self.cursor = self.db.cursor(pymysql.cursors.DictCursor)

    def execute(self, query, args={}):
        self.cursor.execute(query, args)

    def executeOne(self, query, args={}):
        with self.LOCK:
            self.cursor.execute(query, args)
            row = self.cursor.fetchone()
        return row

    def executeAll(self, query, args={}):
        with self.LOCK:
            self.cursor.execute(query, args)
            row = self.cursor.fetchall()
        return row

    def commit(self):
        self.db.commit()
