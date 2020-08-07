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
