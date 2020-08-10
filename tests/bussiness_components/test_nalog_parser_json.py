"""
Файл с тестами экземляра класса ParserNalogJson
"""


def test_parse_organisation_id(correct_accounting_data,
                               incorrect_args,
                               bc_nalog_parser_json,
                               exception_invalid_inn,
                               catch_exception):
    """
    Тест метода parse_organisation_id.
    Реальный ИНН.
    Ожидается: номер организации int.
    """
    test_inn = correct_accounting_data['inn']
    expected_org_id = correct_accounting_data['org_id']

    parse_org_id = bc_nalog_parser_json.parse_organisation_id(test_inn)
    assert isinstance(parse_org_id, str)
    assert parse_org_id == expected_org_id

    test_args = incorrect_args
    for inn in test_args:
        status = catch_exception(bc_nalog_parser_json.parse_organisation_id, exception_invalid_inn, inn)
        assert status


def test_parse_accounting_id(correct_accounting_data,
                             incorrect_args,
                             bc_nalog_parser_json,
                             exception_invalid_org_id,
                             catch_exception):
    """Тест метода parse_accounting_id"""
    test_org_id = correct_accounting_data['org_id']
    expect_acc_id = correct_accounting_data['acc_id']
    parse_acc_id = bc_nalog_parser_json.parse_accounting_id(test_org_id)
    assert isinstance(parse_acc_id, str)
    assert parse_acc_id == expect_acc_id

    test_args = incorrect_args
    for org_id in test_args:
        status = catch_exception(bc_nalog_parser_json.parse_accounting_id, exception_invalid_org_id, org_id)
        assert status


def test_parse_accounting_json(correct_accounting_data,
                               incorrect_args,
                               bc_nalog_parser_json,
                               exception_invalid_acc_id,
                               catch_exception):
    """
    Тест метода parse_accounting_json.
    """
    test_acc_id = correct_accounting_data['acc_id']
    expected_id = correct_accounting_data['id']

    parse_json = bc_nalog_parser_json.parse_accounting_json(test_acc_id)

    assert isinstance(parse_json, list)
    assert parse_json[0].get('id')
    assert str(parse_json[0]['id']) == expected_id

    test_args = incorrect_args
    for acc_id in test_args:
        status = catch_exception(bc_nalog_parser_json.parse_accounting_json, exception_invalid_acc_id, acc_id)
        assert status


def test_parse_accounting(correct_accounting_data,
                          incorrect_args,
                          bc_nalog_parser_json):
    """
    Тест метода parse_accounting
    """
    test_inn = correct_accounting_data['inn']
    expected_id = correct_accounting_data['id']
    parse_json = bc_nalog_parser_json.parse_accounting(test_inn)

    assert isinstance(parse_json, list)
    assert parse_json[0].get('id')
    assert str(parse_json[0]['id']) == expected_id
