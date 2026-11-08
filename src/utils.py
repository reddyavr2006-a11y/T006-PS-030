from datetime import datetime, timedelta


def truncate_4(value):
    return int(value * 10000) / 10000


def calculate_pop_charge(amount):

    charge = amount * 0.005

    if charge < 30:
        charge = 30

    if charge > 25000:
        charge = 25000

    return round(charge, 2)


def is_business_day(date_obj, holidays):

    if date_obj.weekday() >= 5:
        return False

    date_string = date_obj.strftime("%d-%m-%Y")

    for holiday in holidays:

        if holiday["date"] == date_string:
            return False

    return True


def get_next_business_day(date_obj, holidays):

    current = date_obj

    while not is_business_day(current, holidays):
        current += timedelta(days=1)

    return current


def get_nav_for_date(navs, nav_date, scheme):

    for nav in navs:

        if (
            nav["date"] == nav_date
            and nav["scheme"] == scheme
        ):

            return float(nav["nav"])

    return None