from datetime import datetime


def truncate_4(value):
    return int(value * 10000) / 10000


def calculate_pop_charge(amount):

    charge = amount * 0.005

    if charge < 30:
        charge = 30

    if charge > 25000:
        charge = 25000

    return round(charge, 2)


def find_nav(navs, scheme="E"):

    for record in navs:

        if record["scheme"] == scheme:
            return float(record["nav"])

    return None