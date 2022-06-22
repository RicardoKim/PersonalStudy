class OrderRepository:
    def __init__(self, db):
        self.db = db

    def getorder(self):
        SQL = 'SELECT orderNumber, shippedDate, status FROM orders'
        result = self.db.executeAll(SQL)
        return result

    def gettest(self):
        SQL = "SELECT orderNumber, productName,  ProductsCount ,contribution " \
              "FROM (SELECT  orderNumber, productCode, " \
              "(SELECT Count(*) FROM orderdetails WHERE OrderNumber = Main.orderNumber) As 'ProductsCount', " \
              "quantityOrdered*priceEach As 'Product Value', " \
              "(quantityOrdered*priceEach / (SELECT SUM(quantityOrdered*priceEach) FROM orderdetails WHERE orderNumber = Main.orderNumber ))*100 As 'Contribution' " \
              "FROM orderdetails Main ORDER BY  orderNumber )  " \
              "DataTable INNER JOIN products ON products.productCode = DataTable.productCode " \
              "WHERE ProductsCount > 2 AND Contribution > 50"
        result = self.db.executeAll(SQL)
        return

