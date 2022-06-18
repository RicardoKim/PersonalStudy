import json
from flask import request, jsonify, make_response


def create_user_endpoints(app, user_service):
    @app.route('/user', methods=['GET'])
    def get_user():
        users_info = user_service.getuser()
        data = {'error': "", 'status_code': 200, "data": [users_info]}
        return jsonify(data), 200
