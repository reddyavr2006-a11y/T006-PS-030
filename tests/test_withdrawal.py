from src.withdrawal_engine import (
    validate_withdrawal_count
)


def test_withdrawal_allowed():

    result = validate_withdrawal_count(
        2
    )

    assert result[0] is True


def test_withdrawal_rejected():

    result = validate_withdrawal_count(
        3
    )

    assert result[0] is False