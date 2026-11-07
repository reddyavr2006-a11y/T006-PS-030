import os

from loaders import load_subscribers
from loaders import load_commands
from loaders import load_navs
from processor import process_command


project_root = os.path.dirname(os.path.dirname(__file__))

subscribers_path = os.path.join(project_root, "subscribers.csv")
commands_path = os.path.join(project_root, "commands.txt")
navs_path = os.path.join(project_root, "navs.csv")


subscribers = load_subscribers(subscribers_path)
commands = load_commands(commands_path)
navs = load_navs(navs_path)


print("Subscribers Loaded:", len(subscribers))
print("Commands Loaded:", len(commands))
print("NAV Records Loaded:", len(navs))


print("\nFirst Subscriber:\n")
print(subscribers[0])

print("\nFirst NAV Record:\n")
print(navs[0])


print("\nProcessing First 5 Commands:\n")

for command in commands[:5]:
    process_command(command)
    print("-" * 40)