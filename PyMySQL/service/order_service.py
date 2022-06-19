class OrderService:
    def __init__(self, order_repository):
        self.order_repository = order_repository

    def getorder(self):
        orders_info = self.order_repository.getorder()
        return orders_info
