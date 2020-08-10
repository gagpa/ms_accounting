"""
Файл с тестами класса AccountingLogic
"""


def test_get_accounting(correct_accounting_data,
                        incorrect_args,
                        accounting_logic):
    """
    Тест метода get_accounting
    """
    test_inn = correct_accounting_data['inn']
    expect_id = correct_accounting_data['id']
    parse_json = (accounting_logic.get_accounting(test_inn))
    assert isinstance(parse_json, list)
    parse_id = str(parse_json[0]['id'])
    assert expect_id == parse_id
