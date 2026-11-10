def generate_holdings(
        transactions):

    holdings = []

    for row in transactions:

        subscriber_id = row[0]

        tier = row[1]

        nav = float(row[7])

        units = float(row[8])

        value = round(
            units * nav,
            2
        )

        holdings.append([

            subscriber_id,

            tier,

            "E",

            units,

            nav,

            value,

            100
        ])

    return holdings
