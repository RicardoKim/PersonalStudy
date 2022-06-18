class UserRepository:
    def __init__(self, db):
        self.db = db

    def getuser(self):
        SQL = 'SELECT * FROM user'
        result = self.db.executeAll(SQL)
        return result
