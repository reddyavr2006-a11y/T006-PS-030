from exit_engine import (
    calculate_superannuation_exit,
    calculate_premature_exit
)


def generate_exits():

    exits = []

    super_exit = (
        calculate_superannuation_exit(
            500000
        )
    )

    exits.append([

        "SUB-007",

        "2026-09-21",

        "SUPERANNUATION",

        super_exit["status"],

        500000,

        super_exit["lump_sum"],

        super_exit["annuity_purchase"],

        0
    ])

    premature_exit = (
        calculate_premature_exit(
            400000
        )
    )

    exits.append([

        "SUB-012",

        "2026-10-06",

        "PREMATURE",

        premature_exit["status"],

        400000,

        premature_exit["lump_sum"],

        premature_exit["annuity_purchase"],

        0
    ])

    return exits