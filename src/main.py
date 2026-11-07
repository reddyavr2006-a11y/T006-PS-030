import os

project_root = os.path.dirname(os.path.dirname(__file__))
commands_path = os.path.join(project_root, "commands.txt")

with open(commands_path, encoding="utf-8") as file:
    content = file.read()

print("CONTENT OF COMMANDS FILE:")
print("--------------------------------")
print(content[:1000])
print("--------------------------------")