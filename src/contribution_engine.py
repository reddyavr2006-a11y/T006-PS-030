from datetime import datetime, timedelta

from utils import (
    calculate_pop_charge,
    truncate_4,
    get_next_business_day,
    is_business_day,
    get_nav_for_date
)

def process_contribution(
        contribution_id,
        subscriber_id,
        tier,
        date_time,
        contribution_type,
        amount,
        navs,
        holidays):

    amount = float(amount)

    # BR-01

    if tier == "I" and amount < 500:

        print("REJECTED")
        print("Reason: Tier I minimum is ₹500")
        return

    if tier == "II" and amount < 250:

        print("REJECTED")
        print("Reason: Tier II minimum is ₹250")
        return

    # BR-02

    pop_charge = calculate_pop_charge(amount)

    invested_amount = amount - pop_charge

    # BR-03

    received_dt = datetime.strptime(
        date_time,
        "%Y-%m-%d %H:%M:%S"
    )

    cutoff = received_dt.replace(
        hour=9,
        minute=30,
        second=0
    )

    contribution_date = received_dt.date()

    if (
        received_dt < cutoff
        and is_business_day(
            contribution_date,
            holidays
        )
    ):
        nav_date = contribution_date

    else:
        nav_date = get_next_business_day(
            contribution_date + timedelta(days=1),
            holidays
        )

    nav_date_string = nav_date.strftime(
        "%d-%m-%Y"
    )

    nav = get_nav_for_date(
        navs,
        nav_date_string,
        "E"
    )

    if nav is None:

        print("NAV NOT FOUND")
        return

    units = invested_amount / nav

    units = truncate_4(units)

    print("Contribution ID:", contribution_id)
    print("Subscriber:", subscriber_id)

    print("Gross Amount:", amount)

    print("POP Charge:", pop_charge)

    print("Invested Amount:", invested_amount)

    print("NAV Date:", nav_date_string)

    print("NAV Used:", nav)

    print("Units Allocated:", units)