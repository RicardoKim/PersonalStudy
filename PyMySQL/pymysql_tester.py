from threading import Thread
from persistence import customer_repository, order_repository
from db import db_connection
import time

db_instance = db_connection.Database()
customer_repo = customer_repository.UserRepository(db_instance)
order_repo = order_repository.OrderRepository(db_instance)


def call_payment():
    print("payment")
    customer_repo.get_customer_order_info()
    time.sleep(100)
    return


def call_order():
    print("order")
    order_repo.getorder()
    time.sleep(100)
    return


def call_customer_region():
    print("customer")
    customer_repo.get_customer_region('Japan')
    time.sleep(100)
    return


def call_test():
    print("Test")
    order_repo.test()
    time.sleep(100)
    return


def main():
    process_list = []
    temp_p_order = Thread(target=call_order)
    temp_p_payment = Thread(target=call_payment)
    temp_p_region = Thread(target=call_customer_region)
    temp_p_test = Thread(target=call_test)
    temp_p_payment.start()
    temp_p_order.start()
    temp_p_region.start()
    temp_p_test.start()
    process_list.append(temp_p_payment)
    process_list.append(temp_p_order)
    process_list.append(temp_p_region)
    process_list.append(temp_p_test)

    while process_list:
        temp_p = process_list.pop()
        temp_p.join()
    return


if __name__ == "__main__":
    main()
