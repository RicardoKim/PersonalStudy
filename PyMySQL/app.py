from flask import Flask
from db import db_connection
from controller import customer_controller, order_controller
from service import customer_service, order_service
from persistence import customer_repository, order_repository


def create_app():
    app = Flask(__name__)
    db = db_connection.Database()

    customer_repo = customer_repository.UserRepository(db)
    customer_serv = customer_service.UserService(customer_repo)
    customer_controller.create_customer_endpoints(app, customer_serv)

    order_repo = order_repository.OrderRepository(db)
    order_serv = order_service.OrderService(order_repo)
    order_controller.create_order_endpoints(app, order_serv)

    return app
