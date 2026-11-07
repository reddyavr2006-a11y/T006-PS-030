from datetime import datetime, timedelta


def truncate_4(number):
    return int(number * 10000) / 10000


def calculate_pop_charge(amount):

    charge = amount * 0.005

    if charge < 30:
        charge = 30

    if charge > 25000:
        charge = 25000

    return round(charge, 2)


def is_before_cutoff(time_string):

    dt = datetime.strptime(
        time_string,
        "%Y-%m-%d %H:%M:%S"
    )

    cutoff = dt.replace(
        hour=9,
        minute=30,
        second=0
    )

    return dt < cutoff