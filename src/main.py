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
from holdings_engine import (
    generate_holdings
)

from output_manager import (
    write_transactions,
    write_holdings
)
from exits_manager import (
    generate_exits
)
from output_manager import (
    write_transactions,
    write_holdings,
    write_exits
)
from tax_engine import (
    generate_tax_lines
)
from output_manager import (
    write_transactions,
    write_holdings,
    write_exits,
    write_tax_lines
)
from rebalance_manager import (
    generate_rebalances
)
from output_manager import (
    write_transactions,
    write_holdings,
    write_exits,
    write_tax_lines,
    write_rebalances
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
holdings = generate_holdings(
    transactions
)

write_holdings(
    holdings
)
exits = generate_exits()

write_exits(
    exits
)
tax_lines = generate_tax_lines()

write_tax_lines(
    tax_lines
)
rebalances = generate_rebalances()

write_rebalances(
    rebalances
)
print(
    "transactions.csv generated successfully."
)

print(
    "holdings.csv generated successfully."
)

print(
    "exits.csv generated successfully."
)

print(
    "tax_lines.csv generated successfully."
)
print(
    "rebalances.csv generated successfully."
)