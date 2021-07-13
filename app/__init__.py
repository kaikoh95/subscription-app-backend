from flask import Flask, request
from flask_restful_swagger_2 import Api
from flask_cors import CORS
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from flask_apispec.extension import FlaskApiSpec

VERSION = "v1"


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    CORS(app)
    api = Api(app)

    # Create an APISpec
    spec = APISpec(
        title="Customer Subscriptions Api Spec",
        version=VERSION,
        openapi_version="2.0.0",
        plugins=[MarshmallowPlugin()],
        info={
            "description": "Api services and usage guide for Customer Subscriptions",
        }
    )
    app.config.update({
        'APISPEC_SPEC': spec,
        'APISPEC_SWAGGER_URL': '/swagger',  # URI to access API Doc JSON
        'APISPEC_SWAGGER_UI_URL': '/swagger-ui'  # URI to access UI of API Doc
    })
    docs = FlaskApiSpec(app)

    # App environment config
    from app.config.base import BaseConfig
    app.config.from_object(BaseConfig)

    # REST API Resource Views
    from app.customer_subscriptions.views.customer_subscriptions_resource import CustomerSubscriptionsResource

    api.add_resource(CustomerSubscriptionsResource, '/customers/<customer_id>/subscriptions/<subscription_id>')

    # Register specs
    with app.test_request_context():
        docs.register(CustomerSubscriptionsResource)

    # Default routes
    @app.route('/', methods=['GET'])
    def home():
        args = request.args
        out = {
            "message": "Welcome, you can view Swagger docs at /swagger-ui or /swagger."
        }
        if args:
            out = {**out, **args}
        return out, 200, {'Content-Type': 'application/json'}

    # Api Error Handlers
    from app.config.app_error_handlers import app_error_handlers
    app_error_handlers(app)

    return app
