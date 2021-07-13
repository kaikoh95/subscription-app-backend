from marshmallow import Schema, fields


class ProductIdsSchema(Schema):
    ids = fields.String(required=True, example="1,2,3")


class ProductSchema(Schema):
    id = fields.Integer(required=True, example=1)
    name = fields.String(required=True, example="BePure One Daily Multivitamin")
    imageLink = fields.String(required=False, example="")
    price = fields.Float(required=True, example=80.00)
    quantity = fields.Integer(required=False, example=1)


class SubscriptionSchema(Schema):
    id = fields.Integer(required=True, example=15532)
    frequency = fields.Integer(required=False, example=8, default=4)
    products = fields.Nested(ProductSchema(many=True), required=True)


class CustomerSingleSubscriptionSchema(Schema):
    customerId = fields.Integer(required=True, example=10)
    firstName = fields.String(required=True, example="Ben")
    lastName = fields.String(required=True, example="Warren")
    subscription = fields.Nested(SubscriptionSchema(), required=True)


class CustomerResponseSchema(Schema):
    message = fields.String(required=False, example="Message if any")
    data = fields.Nested(CustomerSingleSubscriptionSchema(), required=True)
