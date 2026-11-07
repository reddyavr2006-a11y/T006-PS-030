from loaders import load_subscribers
from loaders import load_commands


subscribers = load_subscribers("../subscribers.csv")
commands = load_commands("../commands.txt")

print("Subscribers Loaded:", len(subscribers))
print("Commands Loaded:", len(commands))

print("\nFirst 2 Subscribers:")
print(subscribers[:2])

print("\nFirst 5 Commands:")

for command in commands[:5]:
    print(command)