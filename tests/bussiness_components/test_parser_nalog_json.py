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
