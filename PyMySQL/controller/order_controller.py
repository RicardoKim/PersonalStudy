from flask import jsonify


def create_order_endpoints(app, order_service):
    @app.route('/order', methods=['GET'])
    def get_order():
        orders_info = order_service.getorder()
        data = {'error': "", 'status_code': 200, "data": [orders_info]}
        return jsonify(data), 200

    @app.route('/order/test', methods=['GET'])
    def get_test():
        test_data = order_service.gettest()
        data = {'error': "", 'status_code': 200, "data": [test_data]}
        return jsonify(data), 200
