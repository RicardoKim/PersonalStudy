from flask import Flask
from db import db_connection
from controller import user_controller
from service import user_service
from persistence import user_repository


def create_app():
    app = Flask(__name__)
    db = db_connection.Database()

    user_repo = user_repository.UserRepository(db)
    user_serv = user_service.UserService(user_repo)
    user_controller.create_user_endpoints(app, user_serv)

    return app
