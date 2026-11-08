import os

from loaders import (
    load_subscribers,
    load_commands,
    load_navs,
    load_holidays
)

from processor import process_command


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

print("Subscribers Loaded:", len(subscribers))
print("Commands Loaded:", len(commands))
print("NAV Records Loaded:", len(navs))
print("Holidays Loaded:", len(holidays))

print("\nProcessing First 5 Commands:\n")

for command in commands[:5]:

    process_command(
        command,
        navs,
        holidays
    )

    print("-" * 40)
from allocation_engine import (
    validate_active_allocation
)

print(
    validate_active_allocation(
        50,
        75,
        15,
        10,
        0
    )
)

print(
    validate_active_allocation(
        51,
        75,
        15,
        10,
        0
    )
)