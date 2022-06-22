class OrderService:
    def __init__(self, order_repository):
        self.order_repository = order_repository

    def getorder(self):
        orders_info = self.order_repository.getorder()
        return orders_info

    def gettest(self):
        test_info = self.order_repository.gettest()
        return test_info