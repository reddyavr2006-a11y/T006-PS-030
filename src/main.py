import os
from loaders import load_subscribers
from loaders import load_commands

project_root = os.path.dirname(os.path.dirname(__file__))

subscribers_path = os.path.join(project_root, "subscribers.csv")
commands_path = os.path.join(project_root, "commands.txt")

subscribers = load_subscribers(subscribers_path)
commands = load_commands(commands_path)

print("Subscribers Loaded:", len(subscribers))
print("Commands Loaded:", len(commands))