class UserService:
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def getuser(self):
        users_info = self.user_repository.getuser()
        return users_info

    def get_customer_order(self):
        customer_order_info = self.user_repository.get_customer_order_info()
        return customer_order_info

    def get_customer_payment(self):
        customer_payment_info_dict = self.user_repository.get_customer_payment()
        customer_payment_info = []
        for customer_info in customer_payment_info_dict :
            customer_payment_info.append({'customer_name' : customer_info['customerName'], 'payment' : str(customer_info['payment'])})
        return customer_payment_info
