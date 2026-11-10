from contribution_engine import process_contribution


def process_command(
        command,
        navs,
        holidays):

    parts = command.split("|")

    command_type = parts[0]

    if command_type == "CONTRIBUTE":

        contribution_id = parts[1]
        subscriber_id = parts[2]
        tier = parts[3]
        date_time = parts[4]
        contribution_type = parts[5]
        amount = parts[6]

        return process_contribution(

            contribution_id,

            subscriber_id,

            tier,

            date_time,

            contribution_type,

            amount,

            navs,

            holidays

        )

    return None