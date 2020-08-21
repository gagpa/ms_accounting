"""
Файл с views с префиксом /api/v1
"""

from . import api
from flask import request, jsonify
from ..bussiness_logics import AccountLogic


@api.route('/accounting')
def accounting():
    inn = request.args.get('inn')
    b_logic = AccountLogic()
    response = b_logic.get_accounting(inn)
    return response


@api.route('/test')
def test():
    print(request.json)
    return 'TEST'
