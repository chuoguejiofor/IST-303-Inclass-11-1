import pytest
@pytest.mark.parametrize("time_period, time_unit, expected", [(1,'day',86400), (1,'month',2592000)])

def test_accuracy(time_period, time_unit, expected):
    assert calc_number_of_seconds(time_period, time_unit) == expected

def test_non_time_units():
    with pytest.raises(Exception):
        calc_number_of_seconds(1, "meter")
