"""
Module to read/update customer subscription data.
This uses a JSON file for persistent storage as requested in the spec.
"""
import json

from app.helpers.exceptions_handlers import exception_handler, LoadFromDbError, SaveToDbError


class CustomerSubscriptionStores:

    def __init__(self, filename, customer_id):
        self.__filename = filename
        self.__customer_id = customer_id
        self.__data = self.__get_json_contents()

    def __get_json_contents(self):
        with open(self.__filename) as file:
            return json.load(file)

    def __set_json_contents(self):
        with open(self.__filename, "w") as file:
            file.write(json.dumps(self.get_customer_data()))

    def get_customer_data(self):
        return self.__data

    def get_customer_specific_subscription(self, subscription_id):
        for subs in self.get_customer_data().get("subscriptions", []):
            if str(subs.get("id")) == subscription_id:
                subs.get("products", []).sort(key=lambda i: i['id'])
                for product in subs.get("products", []):
                    product["quantity"] = product.get("quantity", 1)
                return subs
        return []

    def get_customer_id(self):
        return self.__customer_id

    @exception_handler
    def update_customer_subscription_products(self, subscription_id, products, to_add):
        """
        Simulates db method of updating a subscription.
        Adds a list of Product objects to a specific subscription based on subscription ID.
        """
        for subs in self.get_customer_data().get("subscriptions", []):
            if str(subs.get("id")) == subscription_id:
                for product in products:
                    current_products = subs.get("products", [])
                    self.update_current_products(current_products, product, to_add)
                return self.__set_json_contents()
        error_msg = f"Unable to find Subscription ID {subscription_id} for Customer ID {self.get_customer_id()}"
        raise LoadFromDbError(error_msg)

    def update_current_products(self, current_products, product, to_add):
        modifier = 1 if to_add else -1
        exists = False
        index_to_remove = None
        for i in range(len(current_products)):
            current_product = current_products[i]
            if int(current_product.get("id")) == int(product.get("id")):
                current_product["quantity"] = current_product.get("quantity", 0) + modifier * product.get("quantity", 1)
                if current_product.get("quantity") < 1:
                    index_to_remove = i
                exists = True
                break
        if not exists:
            if not to_add:
                raise SaveToDbError(f"Unable to remove Product ID {product.get('id')} from Customer ID "
                                    f"{self.get_customer_id()} subscription list")
            product["quantity"] = product.get("quantity", 1)
            current_products.append(product)
        if index_to_remove is not None:
            current_products.pop(index_to_remove)
