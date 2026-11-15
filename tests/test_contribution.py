from src.utils import calculate_pop_charge


def test_pop_charge_minimum():
    assert calculate_pop_charge(5000) == 30


def test_pop_charge_percentage():
    assert calculate_pop_charge(15000) == 75
