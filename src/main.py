import os

from loaders import load_subscribers
from loaders import load_commands
from processor import process_command


# Project root folder
project_root = os.path.dirname(os.path.dirname(__file__))

# Build paths
subscribers_path = os.path.join(project_root, "subscribers.csv")
commands_path = os.path.join(project_root, "commands.txt")

# Load files
subscribers = load_subscribers(subscribers_path)
commands = load_commands(commands_path)

# Display statistics
print("Subscribers Loaded:", len(subscribers))
print("Commands Loaded:", len(commands))

# Display first two subscribers
print("\nFirst 2 Subscribers:\n")
print(subscribers[:2])

# Process first five commands
print("\nProcessing First 5 Commands:\n")

for command in commands[:5]:
    process_command(command)
    print("-" * 40)