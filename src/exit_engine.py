def calculate_superannuation_exit(
        corpus):

    if corpus <= 500000:

        return {
            "lump_sum": corpus,
            "annuity_purchase": 0,
            "status": "100% Lump Sum Allowed"
        }

    lump_sum = corpus * 0.60

    annuity_purchase = corpus * 0.40

    return {
        "lump_sum": lump_sum,
        "annuity_purchase": annuity_purchase,
        "status": "40% Annuity Required"
    }


def calculate_premature_exit(
        corpus):

    if corpus <= 250000:

        return {
            "lump_sum": corpus,
            "annuity_purchase": 0,
            "status": "100% Lump Sum Allowed"
        }

    lump_sum = corpus * 0.20

    annuity_purchase = corpus * 0.80

    return {
        "lump_sum": lump_sum,
        "annuity_purchase": annuity_purchase,
        "status": "80% Annuity Required"
    }


def find_annuity_rate(
        annuity_rates,
        age,
        option):

    for row in annuity_rates:

        if (
            int(row["age"]) == age
            and row["option"] == option
        ):

            return float(
                row["rate_per_1000_per_year"]
            )

    return None


def calculate_monthly_annuity(
        purchase_price,
        rate):

    annual_annuity = (
        purchase_price *
        rate
    ) / 1000

    monthly_annuity = (
        annual_annuity / 12
    )

    monthly_annuity = int(
        monthly_annuity * 100
    ) / 100

    return monthly_annuity
def exit_precedence():

    steps = [

        "Freeze Check",

        "Eligibility Check",

        "Corpus Threshold",

        "Annuity Minimum",

        "Lump Sum",

        "Tax Processing"
    ]

    return steps