import os

from loaders import (
    load_subscribers,
    load_commands,
    load_navs,
    load_holidays
)

from processor import (
    process_command
)

from output_manager import (
    write_transactions
)


project_root = os.path.dirname(
    os.path.dirname(__file__)
)


subscribers_path = os.path.join(
    project_root,
    "subscribers.csv"
)

commands_path = os.path.join(
    project_root,
    "commands.txt"
)

navs_path = os.path.join(
    project_root,
    "navs.csv"
)

holidays_path = os.path.join(
    project_root,
    "holidays.csv"
)


subscribers = load_subscribers(
    subscribers_path
)

commands = load_commands(
    commands_path
)

navs = load_navs(
    navs_path
)

holidays = load_holidays(
    holidays_path
)


print(
    "Subscribers Loaded:",
    len(subscribers)
)

print(
    "Commands Loaded:",
    len(commands)
)

print(
    "NAV Records Loaded:",
    len(navs)
)

print(
    "Holidays Loaded:",
    len(holidays)
)


transactions = []


for command in commands[:10]:

    result = process_command(

        command,

        navs,

        holidays
    )

    if result:

        transactions.append(
            result
        )


write_transactions(
    transactions
)


print(
    "\ntransactions.csv generated successfully."
)

print(
    "Transaction Count:",
    len(transactions)
)