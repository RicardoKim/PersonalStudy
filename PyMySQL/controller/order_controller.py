from flask import jsonify


def create_order_endpoints(app, order_service):
    @app.route('/order', methods=['GET'])
    def get_order():
        orders_info = order_service.getorder()
        data = {'error': "", 'status_code': 200, "data": [orders_info]}
        return jsonify(data), 200

