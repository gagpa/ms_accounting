from . import api
from flask import request, jsonify
from ..bussiness_logics import AccountLogic
from ..exceptions.invalid_app import InternalError
from ..exceptions.invalid_data import InvalidInn


@api.route('/accounting')
def accounting():
    inn = request.args.get('inn')
    b_logic = AccountLogic()
    try:
        accounting_dict = b_logic.get_accounting(inn)
        return jsonify({
            'success': True,
            'data': accounting_dict
        })
    except InvalidInn:
        return jsonify({
            'success': False,
            'message': 'Не верный ИНН'
        })
    except InternalError:
        return jsonify({
            'success': False,
            'message': 'Сервис не доступен'
        })
