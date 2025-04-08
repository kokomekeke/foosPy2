from marshmallow import post_load


from server.models.transaction_type import TransactionType
from server.models.transactions import TransactionSchema, Transaction


class Income(Transaction):
    def __init__(self, description, amount):
        super(Income, self).__init__(description, amount, 0, TransactionType.INCOME)

    def __repr__(self):
        return '<Income(name={self.description!r})>'.format(self=self)


class IncomeSchema(TransactionSchema):
    @post_load
    def make_income(self, data, **kwargs):
        return Income(**data)