from src.exit_engine import (
    calculate_superannuation_exit,
    calculate_premature_exit
)


def test_superannuation_threshold():

    result = calculate_superannuation_exit(
        500000
    )

    assert result[
        "annuity_purchase"
    ] == 0


def test_premature_exit():

    result = calculate_premature_exit(
        400000
    )

    assert result[
        "annuity_purchase"
    ] == 320000