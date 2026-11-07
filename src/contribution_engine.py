from utils import calculate_pop_charge
from utils import truncate_4
from utils import find_nav


def process_contribution(
        contribution_id,
        subscriber_id,
        tier,
        date_time,
        contribution_type,
        amount,
        navs):

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

    nav = find_nav(navs, "E")

    units = invested_amount / nav

    units = truncate_4(units)

    print("Contribution ID:", contribution_id)
    print("Subscriber:", subscriber_id)

    print("Gross Amount:", amount)

    print("POP Charge:", pop_charge)

    print("Invested Amount:", invested_amount)

    print("NAV Used:", nav)

    print("Units Allocated:", units)