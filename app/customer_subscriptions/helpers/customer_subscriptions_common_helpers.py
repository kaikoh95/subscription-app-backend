from app.customer_subscriptions.stores.stores import CustomerSubscriptionStores


class CustomerSubscriptionsCommonHelpers:

    def __init__(self, customer_id):
        self.customer = CustomerSubscriptionStores(filename="stores.json", customer_id=customer_id)

    def update_customer_subscription_products(self, subscription_id, products, to_add=False):
        self.customer.update_customer_subscription_products(subscription_id=subscription_id, products=products, to_add=to_add)
        return self.get_customer_data(subscription_id=subscription_id)

    def get_customer_data(self, subscription_id):
        customer_data = {k: v for k, v in self.customer.get_customer_data().items()}
        subscription = self.customer.get_customer_specific_subscription(subscription_id=subscription_id)
        customer_data.pop("subscriptions")
        return {
            **customer_data,
            "subscription": subscription,
        }
