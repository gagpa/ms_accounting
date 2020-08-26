from app import serializer


class PeriodsField(serializer.Field):
    times = ('current', 'previous', 'beforePrevious')

    def _serialize(self, value: str, attr, obj, **kwargs):
        period = obj['period']
        new_data = []
        for _ in self.times:
            new_data.append(period)
            period = str(int(period) - 1)
        new_data.reverse()
        return new_data
