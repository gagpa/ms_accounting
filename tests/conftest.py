import init_env

import json
import pytest
from app.bussiness_components import AccountingEntity


@pytest.fixture()
def accounting_entity():
    """
    Объект БО для связи с БД.
    """
    return AccountingEntity


@pytest.fixture()
def inn():
    """
    ИНН.
    """
    return '5405956474'


@pytest.fixture()
def period_accounting():
    """
    Период БО.
    """
    return '2019'


@pytest.fixture()
def nalog_accounting():
    """
    БО с bo.nalog.ru
    """
    with open('tests/nalog_accounting.json') as f:
        accounting = json.load(f)
    return accounting
