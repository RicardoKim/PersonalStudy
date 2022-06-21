class UserRepository:
    def __init__(self, db):
        self.db = db

    def getuser(self):
        sql = 'SELECT customerNumber FROM customers'
        result = self.db.executeAll(sql)
        return result

    def get_customer_order_info(self):
        sql = 'SELECT c.customerName, p.productName FROM customers c, orders o, orderdetails d, products p ' \
              'WHERE c.customerNumber = o.customerNumber ' \
              'and o.orderNumber = d.orderNumber ' \
              'and d.productCode = p.productCode'
        result = self.db.executeAll(sql)
        return result

    def get_customer_payment(self):
        sql = 'SELECT c.customerName AS customerName, SUM(p.amount) AS payment FROM customers c, payments p WHERE c.customerNumber = p.customerNumber GROUP BY customerName'
        result = self.db.executeAll(sql)
        print(result)
        return result

    def get_customer_region(self, region):
        SQL ="SELECT productName FROM products INNER JOIN orderdetails od on products.productCode = od.productCode INNER JOIN orders o on od.orderNumber = o.orderNumber INNER JOIN customers c on o.customerNumber = c.customerNumber WHERE c.customerName = 'Herkku Gifts'"
        self.db.executeAll(SQL)
        return