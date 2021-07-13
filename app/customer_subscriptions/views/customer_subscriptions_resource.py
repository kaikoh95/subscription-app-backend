from app.customer_subscriptions.helpers.customer_subscriptions_common_helpers import CustomerSubscriptionsCommonHelpers
from app.customer_subscriptions.schemas.customer_subscriptions_schemas import ProductSchema, \
    ProductIdsSchema, CustomerResponseSchema
from app.helpers.common_helpers import process_request_body, convert_to_camel_case
from flask_apispec.views import MethodResource
from flask_apispec import marshal_with, doc, use_kwargs


class CustomerSubscriptionsResource(MethodResource):

    @doc(description="Gets a customer's subscription data from the local file storage.",
         tags=["Customer Subscription"])
    @marshal_with(CustomerResponseSchema, description="Returns Customer data.", code=200)
    def get(self, **kwargs):
        customer_id = kwargs.get("customer_id")
        subscription_id = kwargs.get("subscription_id")

        customer_data = CustomerSubscriptionsCommonHelpers(customer_id=customer_id)\
            .get_customer_data(subscription_id=subscription_id)
        response = {"data": convert_to_camel_case(customer_data)}
        return response, 200

    @doc(description="Updates a customer's subscription data and saves it in the local file storage.",
         tags=["Customer Subscription"])
    @use_kwargs(ProductSchema(many=True), location="json", description="Accepts single or multiple products data.")
    @marshal_with(CustomerResponseSchema, description="Returns Customer data.", code=200)
    def put(self, args, **kwargs):
        products = process_request_body(ProductSchema(many=True))
        customer_id = kwargs.get("customer_id")
        subscription_id = kwargs.get("subscription_id")

        customer_data = CustomerSubscriptionsCommonHelpers(customer_id=customer_id)\
            .update_customer_subscription_products(subscription_id=subscription_id, products=products, to_add=True)
        response = {
            "message": "Updated customer subscription data.",
            "data": convert_to_camel_case(customer_data),
        }
        return response, 200

    @doc(description="Deletes the first occurrence of the product ID from a customer's subscription data "
                     "and saves it in the local file storage.",
         tags=["Customer Subscription"])
    @use_kwargs(ProductIdsSchema(), location="json", description="Accepts a string of comma-separated product IDs.")
    @marshal_with(CustomerResponseSchema, description="Returns Customer data.", code=200)
    def delete(self, **kwargs):
        customer_id = kwargs.get("customer_id")
        subscription_id = kwargs.get("subscription_id")
        product_id = kwargs.get("ids", "")
        products = [{"id": product_id}]

        customer_data = CustomerSubscriptionsCommonHelpers(customer_id=customer_id)\
            .update_customer_subscription_products(subscription_id=subscription_id, products=products)
        response = {
            "message": f"Removed 1 x product {product_id} from customer subscription data.",
            "data": convert_to_camel_case(customer_data),
        }
        return response, 200
