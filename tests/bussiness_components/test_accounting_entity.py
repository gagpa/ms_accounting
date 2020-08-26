def test_save_delete_exist(accounting_entity, inn, period_accounting, nalog_accounting):
    assert not accounting_entity.exist(inn)
    model = accounting_entity(inn, period_accounting, nalog_accounting)
    model.save()
    assert model.exist(inn)
    model.delete()
    assert not model.exist(inn)


def test_get_object():
    pass


def test_get_dict():
    pass
