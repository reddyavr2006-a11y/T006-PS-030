import csv

def load_subscribers(file_path):
    subscribers = []

    with open(file_path, encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter="\t")

        for row in reader:
            subscribers.append(row)

    return subscribers
def load_commands(file_path):
    commands = []

    with open(file_path, encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if line:
                commands.append(line)

    return commands