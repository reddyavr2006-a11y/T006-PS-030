def validate_active_allocation(
        age,
        e_pct,
        c_pct,
        g_pct,
        a_pct):

    total = (
        e_pct +
        c_pct +
        g_pct +
        a_pct
    )

    if total != 100:
        return (
            False,
            "Allocation must sum to 100"
        )

    if a_pct > 5:
        return (
            False,
            "Alternative assets exceed 5%"
        )

    if age <= 50:

        max_equity = 75

    else:

        reduction = (
            age - 50
        ) * 2.5

        max_equity = 75 - reduction

        if max_equity < 50:
            max_equity = 50

    if e_pct > max_equity:

        return (
            False,
            f"Maximum equity allowed is {max_equity}%"
        )

    return (
        True,
        "Valid Allocation"
    )