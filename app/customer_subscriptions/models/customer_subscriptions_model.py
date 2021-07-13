from datetime import datetime
from app.helpers.common_helpers import convert_to_camel_case


class CustomerSubscriptionsModel:
    customer_id = None
    first_name = None
    last_name = None
    subscriptions = None

    def __init__(self, iterable=(), **kwargs):
        self.__dict__.update(iterable, **kwargs)

    def serialize(self):
        """Converts model into readable format in camel case"""
        data = {
            # "id": self.id,
            # "object_id": self.object_id,
            # "object_number": self.object_number,
            # "object_status": self.object_status,
            # "last_location": {
            #     "lat": self.lat,
            #     "long": self.long,
            # }
        }
        return convert_to_camel_case(data)
