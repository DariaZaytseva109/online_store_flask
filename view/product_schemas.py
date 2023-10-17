from marshmallow import Schema, fields, validate


class ProductSchema(Schema):
    id = fields.String()
    name = fields.String(required=True, validate=validate.Length(min=3))
    price = fields.Float(required=True, validate=validate.Range(min=1, max=300000))


class ProductGetManyParams(Schema):
    page = fields.Int(required=True, validate=validate.Range(min=1))
    limit = fields.Int(required=True, validate=validate.Range(min=3, max=20))
