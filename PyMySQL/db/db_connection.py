from pymysqlpool.pool import Pool
from threading import RLock

class Database():
    def __init__(self):
        self.LOCK = RLock()
        self.db_config = {
            "host" : "",
            "port" : "",
            "database" : "",
            "password" : "",
            "user" : ""
        }
        self.pool = Pool(**self.db_config)
        self.pool.init()

    def execute(self, query, args={}):
        connection = self.pool.get_conn()
        cursor = connection.cursor()
        cursor.execute(query, args)
        res = cursor.fetchall()
        self.pool.release(connection)
        return res
