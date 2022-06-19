class OrderRepository:
    def __init__(self, db):
        self.db = db

    def getorder(self):
        SQL = 'SELECT orderNumber, shippedDate, status FROM orders'
        result = self.db.executeAll(SQL)
        return result
