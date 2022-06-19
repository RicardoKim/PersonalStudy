from multiprocessing import Process
from persistence import customer_repository, order_repository
from db import db_connection

def call_payment():
    db_instance = db_connection.Database()
    cr = customer_repository.UserRepository(db_instance)
    output = cr.get_customer_order_info()
    print("Payment")
    return

def call_order():
    db_instance = db_connection.Database()
    order_repo = order_repository.OrderRepository(db_instance)
    output = order_repo.getorder()
    print("Order")
    return

def main():
    process_list = []
    for i in range(1000):
        temp_p_order = Process(target=call_order)
        temp_p_payment = Process(target=call_payment)
        temp_p_payment.start()
        temp_p_order.start()
        process_list.append(temp_p_payment)
        process_list.append(temp_p_order)

    while process_list :
        temp_p = process_list.pop()
        temp_p.join()
    return


if __name__ == "__main__":
    main()
