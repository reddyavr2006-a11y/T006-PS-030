from datetime import datetime


ALLOWED_PURPOSES = {

    "CHILD_EDUCATION",

    "CHILD_MARRIAGE",

    "HOUSE_PURCHASE",

    "MEDICAL",

    "SKILL_DEVELOPMENT",

    "STARTUP"
}


def validate_withdrawal_purpose(
        purpose):

    if purpose not in ALLOWED_PURPOSES:

        return (
            False,
            "Invalid Purpose"
        )

    return (
        True,
        "Valid Purpose"
    )


from datetime import datetime


def validate_three_year_rule(
        join_date,
        withdrawal_date):

    join_date = datetime.strptime(
        join_date,
        "%Y-%m-%d"
    ).date()

    withdrawal_date = datetime.strptime(
        withdrawal_date,
        "%Y-%m-%d"
    ).date()

    third_anniversary = join_date.replace(
        year=join_date.year + 3
    )

    if withdrawal_date < third_anniversary:

        return (
            False,
            "3 years not completed"
        )

    return (
        True,
        "Eligible"
    )