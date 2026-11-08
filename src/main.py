from loaders import load_glide_paths

from allocation_engine import (
    get_target_allocation
)
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
glide_path_file = os.path.join(
    project_root,
    "glidepath.csv"
)

glide_paths = load_glide_paths(
    glide_path_file
)

print(
    get_target_allocation(
        glide_paths,
        "LC75",
        36
    )
)