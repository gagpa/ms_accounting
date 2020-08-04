import pytest

from app.bussiness_components.parser_nalog_json import ParserNalogJson, InvalidInn


@pytest.fixture()
def bc_parser_nalog_json():
    return ParserNalogJson()


@pytest.fixture()
def exception_invalid_inn():
    return InvalidInn
