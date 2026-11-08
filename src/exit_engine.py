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