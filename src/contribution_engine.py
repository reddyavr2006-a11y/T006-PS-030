from utils import calculate_pop_charge
from utils import truncate_4


def process_contribution(
        contribution_id,
        subscriber_id,
        tier,
        date_time,
        contribution_type,
        amount):

    amount = float(amount)

    if tier == "I" and amount < 500:

        print("REJECTED")
        print("Reason: Tier I minimum is 500")
        return

    if tier == "II" and amount < 250:

        print("REJECTED")
        print("Reason: Tier II minimum is 250")
        return

    pop_charge = calculate_pop_charge(amount)

    invested_amount = amount - pop_charge

    print("Contribution ID:", contribution_id)
    print("Subscriber:", subscriber_id)

    print("Gross Amount:", amount)

    print("POP Charge:", pop_charge)

    print("Invested Amount:",
          round(invested_amount, 2))