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


def test_parse_organisation_id(bc_parser_nalog_json, exception_invalid_inn):
    """
    Тест метода parse_organisation_id.
    Реальный ИНН.
    Ожидается: номер организации int.
    """
    test_inn = '5405956474'

    expected_org_id = 9192266

    parse_org_id = bc_parser_nalog_json.parse_organisation_id(test_inn)
    assert isinstance(parse_org_id, int)
    assert parse_org_id == expected_org_id

    test_inn = '123'
    status = False
    try:
        bc_parser_nalog_json.parse_organisation_id(test_inn)
    except exception_invalid_inn:
        status = True
    assert status

    test_inn = (1, 2, 3)
    status = False
    try:
        bc_parser_nalog_json.parse_organisation_id(test_inn)
    except exception_invalid_inn:
        status = True
    assert status

    test_inn = None
    status = False
    try:
        bc_parser_nalog_json.parse_organisation_id(test_inn)
    except exception_invalid_inn:
        status = True
    assert status


def test_parse_accounting_id(bc_parser_nalog_json, exception_invalid_org_id):
    """Тест метода parse_accounting_id"""
    test_org_id = '9192266'
    expect_acc_id = 1714957
    parse_acc_id = bc_parser_nalog_json.parse_accounting_id(test_org_id)
    assert isinstance(parse_acc_id, int)
    assert parse_acc_id == expect_acc_id

    test_org_id = (1, 2, 3)
    status = False
    try:
        bc_parser_nalog_json.parse_accounting_id(test_org_id)
    except exception_invalid_org_id:
        status = True
    assert status

    test_org_id = '123'
    status = False
    try:
        bc_parser_nalog_json.parse_accounting_id(test_org_id)
    except exception_invalid_org_id:
        status = True
    assert status


def test_parse_accounting_json(bc_parser_nalog_json, exception_invalid_acc_id):
    """
    Тест метода parse_accounting_json.
    """
    test_acc_id = '1714957'
    expected_id = 3303297

    parse_json = bc_parser_nalog_json.parse_accounting_json(test_acc_id)

    assert isinstance(parse_json, list)
    assert parse_json[0].get('id')
    assert parse_json[0]['id'] == expected_id

    test_acc_id = (1, 2, 3)
    status = False
    try:
        bc_parser_nalog_json.parse_accounting_json(test_acc_id)
    except exception_invalid_acc_id:
        status = True
    assert status

    test_acc_id = ''
    status = False
    try:
        bc_parser_nalog_json.parse_accounting_json(test_acc_id)
    except exception_invalid_acc_id:
        status = True
    assert status

    test_acc_id = None
    status = False
    try:
        bc_parser_nalog_json.parse_accounting_json(test_acc_id)
    except exception_invalid_acc_id:
        status = True
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
