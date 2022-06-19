from flask import jsonify


def create_customer_endpoints(app, customer_service):
    @app.route('/customer', methods=['GET'])
    def get_user():
        customers_info = customer_service.getuser()
        data = {'error': "", 'status_code': 200, "data": [customers_info]}
        return jsonify(data), 200

    @app.route('/customer/order', methods=['GET'])
    def get_customer_order():
        customer_order_info = customer_service.get_customer_order()
        data = {'error': "", 'status_code': 200, "data": [customer_order_info]}
        return jsonify(data), 200

    @app.route('/customer/payment', methods = ['GET'])
    def get_customer_payment():
        customer_payment = customer_service.get_customer_payment()
        data = {'error': "", 'status_code': 200, "data": [customer_payment]}
        return jsonify(data), 200