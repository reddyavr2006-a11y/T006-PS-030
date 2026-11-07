import os

from loaders import load_subscribers
from loaders import load_commands
from processor import process_command


# Get project root directory
project_root = os.path.dirname(os.path.dirname(__file__))

# Build file paths
subscribers_path = os.path.join(project_root, "subscribers.csv")
commands_path = os.path.join(project_root, "commands.txt")

# Load data
subscribers = load_subscribers(subscribers_path)
commands = load_commands(commands_path)

# Display basic info
print("Subscribers Loaded:", len(subscribers))
print("Commands Loaded:", len(commands))

# Show first 2 subscribers
print("\nFirst 2 Subscribers:")
print(subscribers[:2])

# Process first 5 commands
print("\nProcessing First 5 Commands:\n")

for command in commands[:5]:
    process_command(command)
    print("-" * 40)