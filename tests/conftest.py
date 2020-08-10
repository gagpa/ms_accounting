"""
Файл с фиктурами для тестов.
"""
import pytest

from app.bussiness_components.exceptions.invalid_data import InvalidInn, InvalidOrgId, InvalidAccId
from app.bussiness_components.nalog_parser_json import NalogParserJson
from app.bussiness_components.nalog_scalper import NalogScalper
from app.bussiness_logics.account_logic import AccountLogic


@pytest.fixture()
def bc_nalog_parser_json():
    return NalogParserJson()


@pytest.fixture()
def exception_invalid_inn():
    return InvalidInn


@pytest.fixture()
def exception_invalid_org_id():
    return InvalidOrgId


@pytest.fixture()
def exception_invalid_acc_id():
    return InvalidAccId


@pytest.fixture()
def catch_exception():
    def catch_exception(arg, bc_method, exception):
        status = False
        try:
            bc_method(arg)
        except exception:
            status = True
        return status

    return catch_exception


@pytest.fixture()
def correct_accounting_data():
    data = {
        'inn': '5405956474',
        'org_id': '9192266',
        'acc_id': '1714957',
        'id': '3303297',
    }
    return data


@pytest.fixture()
def incorrect_args():
    args = ('', None, False, {}, [], (), '-5405956474', '123', 123)
    return args


@pytest.fixture()
def search_link():
    return 'https://bo.nalog.ru/nbo/organizations/search?query=5405956474'


@pytest.fixture()
def accounting_logic():
    return AccountLogic()


@pytest.fixture()
def bc_nalog_scalper():
    return NalogScalper()
