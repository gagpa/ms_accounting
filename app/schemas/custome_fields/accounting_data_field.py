from collections import defaultdict

from marshmallow import ValidationError

from app import serializer


class AccountingDataField(serializer.Field):
    """
    Кастомное поле для данных БО.
    """
    times = ('current', 'previous', 'beforePrevious')

    def _serialize(self, value: dict, attr, obj, **kwargs):
        new_data = defaultdict(dict)
        period = obj['period']
        periods = self.transform_period(period)
        for collection in value.values():
            if isinstance(collection, dict):
                for key, inner_value in collection.items():
                    obj_word_time, new_key = self.separate_key(key)
                    if obj_word_time in self.times:
                        translate_key = periods[obj_word_time]
                        new_data[translate_key].update({new_key: inner_value or None})
        return new_data

    def _deserialize(self, value, attr, data, **kwargs):
        raise ValidationError("Pin codes must contain only digits.")

    def transform_period(self, period: str):
        translate_period = {}
        for time in self.times:
            date = period
            translate_period[time] = date
            period = str(int(period) - 1)
        return translate_period

    def separate_key(self, key):
        for i, sign in enumerate(reversed(key)):
            if not sign.isdigit():
                return key[:-i], key[-i:]
