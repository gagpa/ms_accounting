"""
Файл с тестами класса NalogValidatorInfo
"""


def test_validate_parse_inn(correct_accounting_data,
                            incorrect_args,
                            bc_nalog_validator_info,
                            exception_invalid_inn,
                            catch_exception):
    """Тест метода validate_parse_inn"""
    test_inn = correct_accounting_data['inn']
    status = catch_exception(bc_nalog_validator_info.validate_parse_inn, exception_invalid_inn, test_inn, test_inn)
    assert not status
    test_args = incorrect_args
    for inn in test_args:
        status = catch_exception(bc_nalog_validator_info.validate_parse_inn, exception_invalid_inn, inn, test_inn)
        assert status


def test_validate_inn(correct_accounting_data,
                      incorrect_args,
                      bc_nalog_validator_info,
                      exception_invalid_inn,
                      catch_exception):
    """
    Тест метода validate_inn.
    """
    test_inn = correct_accounting_data['inn']
    status = catch_exception(bc_nalog_validator_info.validate_inn, exception_invalid_inn, test_inn)
    assert not status
    for inn in incorrect_args:
        status = catch_exception(bc_nalog_validator_info.validate_inn, exception_invalid_inn, inn)
        assert status


def test_validate_organisation_json(correct_accounting_data,
                                    incorrect_args,
                                    bc_nalog_validator_info,
                                    exception_invalid_org_id,
                                    catch_exception):
    """
    Тест метода validate_organisation_json.
    """
    test_json = [{'1': '1'}]
    status = catch_exception(bc_nalog_validator_info.validate_organisation_json, exception_invalid_org_id, test_json)
    assert not status
