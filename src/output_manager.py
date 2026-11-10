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