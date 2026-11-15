import csv


def write_transactions(transactions):

    with open(
        "transactions.csv",
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            "subscriber_id",
            "tier",
            "txn_id",
            "event_date",
            "gross_amount",
            "pop_charge",
            "invested_amount",
            "nav",
            "units",
            "status"
        ])

        for transaction in transactions:
            writer.writerow(transaction)


def write_holdings(holdings):

    with open(
        "holdings.csv",
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            "subscriber_id",
            "tier",
            "scheme",
            "units",
            "nav",
            "value",
            "pct"
        ])

        for holding in holdings:
            writer.writerow(holding)


def write_exits(exits):

    with open(
        "exits.csv",
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            "subscriber_id",
            "exit_date",
            "type",
            "status",
            "corpus",
            "lump_sum",
            "annuity_purchase",
            "monthly_annuity"
        ])

        for row in exits:
            writer.writerow(row)


def write_tax_lines(tax_lines):

    with open(
        "tax_lines.csv",
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            "subscriber_id",
            "financial_year",
            "line_type",
            "amount",
            "tax_rate",
            "tax"
        ])

        for row in tax_lines:
            writer.writerow(row)
def write_rebalances(rebalances):

    with open(
        "rebalances.csv",
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        writer.writerow([

            "subscriber_id",

            "birthday",

            "completed_age",

            "fund",

            "scheme",

            "target_pct",

            "actual_pct_before",

            "deviation",

            "action"
        ])

        for row in rebalances:

            writer.writerow(row)