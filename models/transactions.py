from marshmallow import Schema, fields


class Transaction(object):
    def __init__(self, description, amount, created_at, type):
        self.description = description
        self.amount = amount
        self.created_at = created_at
        self.type = type

    def __repr__(self):
        return '<Transaction(name={self.description})>'.format(self=self)


class TransactionSchema(Schema):
    description = fields.Str()
    amount = fields.Number()
    created_at = fields.Date()
    type = fields.Str()