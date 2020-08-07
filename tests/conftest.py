import pytest

from app.bussiness_components.parser_nalog_json import ParserNalogJson, InvalidInn, InvalidOrgId, InvalidAccId


@pytest.fixture()
def bc_parser_nalog_json():
    return ParserNalogJson()


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
