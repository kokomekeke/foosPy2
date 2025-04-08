from flask import Flask, jsonify, request, Blueprint


incomes_bp = Blueprint('incomes', __name__)

incomes = [
    {'description': 'salary', 'amount': 5000}
]


@incomes_bp.route('/incomes')
def get_incomes():
    return jsonify(incomes)


@incomes_bp.route('/incomes', methods=['POST'])
def add_income():
    incomes.append(request.get_json())
    return '', 204