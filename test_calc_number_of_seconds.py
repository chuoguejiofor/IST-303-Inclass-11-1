import pytest
@fixture.mark.parameterize("time_period, time_unit, expected", [(1,'day',86400), (1,'month',2592000)])

def test_accuracy(time_period, time_unit, expected):
    assert calc_number_of_seconds(time_period, time_unit) == expected
