"""
Файл с views с префиксом /api/v1
"""

from flask import request

from . import api
from ..bussiness_logics import AccountingLogic


@api.route('/accounting')
def accounting():
    inn = request.args.get('inn')
    token = request.headers.get('Authorization')
    b_logic = AccountingLogic()
    response = b_logic.get_accounting(inn, token)
    return response


@api.route('/test')
def test():
    print(request.json)
    return 'TEST'
