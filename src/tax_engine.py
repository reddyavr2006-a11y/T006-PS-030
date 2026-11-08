def calculate_employer_excess_tax(
        basic_salary,
        employer_contribution):

    taxable_limit = (
        basic_salary * 0.10
    )

    if employer_contribution <= taxable_limit:

        return {
            "taxable_amount": 0,
            "status": "No Tax"
        }

    excess = (
        employer_contribution -
        taxable_limit
    )

    return {
        "taxable_amount": excess,
        "status": "Taxable"
    }