"""
Файл с тестами экземляра класса ParserNalogJson
"""


def test_get_request(bc_parser_nalog_json):
    """
    Тест метода get_request.
    test_link - реальная ссылка на json.
    Ожидается: 200 статус код int.
    """
    test_link = 'https://bo.nalog.ru/nbo/organizations/search?query=5405956474'
    response = bc_parser_nalog_json.get_request(test_link)
    expect_status_code = 200
    assert response.status_code == expect_status_code


def test_parse_organisation_id(bc_parser_nalog_json, exception_invalid_inn, catch_exception):
    """
    Тест метода parse_organisation_id.
    Реальный ИНН.
    Ожидается: номер организации int.
    """
    test_inn = '5405956474'
    expected_org_id = '9192266'

    parse_org_id = bc_parser_nalog_json.parse_organisation_id(test_inn)
    assert isinstance(parse_org_id, str)
    assert parse_org_id == expected_org_id

    test_args = ['123', (1, 2, 3), None, '']
    for inn in test_args:
        status = catch_exception(inn, bc_parser_nalog_json.parse_organisation_id, exception_invalid_inn)
        assert status


def test_parse_accounting_id(bc_parser_nalog_json, exception_invalid_org_id, catch_exception):
    """Тест метода parse_accounting_id"""
    test_org_id = '9192266'
    expect_acc_id = '1714957'
    parse_acc_id = bc_parser_nalog_json.parse_accounting_id(test_org_id)
    assert isinstance(parse_acc_id, str)
    assert parse_acc_id == expect_acc_id

    test_args = ['123', (1, 2, 3), None, '']
    for org_id in test_args:
        status = catch_exception(org_id, bc_parser_nalog_json.parse_accounting_id, exception_invalid_org_id)
        assert status


def test_parse_accounting_json(bc_parser_nalog_json, exception_invalid_acc_id, catch_exception):
    """
    Тест метода parse_accounting_json.
    """
    test_acc_id = '1714957'
    expected_id = 3303297

    parse_json = bc_parser_nalog_json.parse_accounting_json(test_acc_id)

    assert isinstance(parse_json, list)
    assert parse_json[0].get('id')
    assert parse_json[0]['id'] == expected_id

    test_args = ['123', (1, 2, 3), None, '']
    for acc_id in test_args:
        status = catch_exception(acc_id, bc_parser_nalog_json.parse_accounting_json, exception_invalid_acc_id)
        assert status


def test_parse_accounting(bc_parser_nalog_json):
    """
    Тест метода parse_accounting
    """
    test_inn = '5405956474'
    expected_id = 3303297
    parse_json = bc_parser_nalog_json.parse_accounting(test_inn)

    assert isinstance(parse_json, list)
    assert parse_json[0].get('id')
    assert parse_json[0]['id'] == expected_id
