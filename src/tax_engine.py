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


def generate_tax_lines():

    tax_lines = []

    result = calculate_employer_excess_tax(
        50000,
        6000
    )

    tax_lines.append([

        "SUB-010",

        "2025-26",

        "EMPLOYER_EXCESS",

        result["taxable_amount"],

        "AS_PER_SLAB",

        result["taxable_amount"]
    ])

    return tax_lines