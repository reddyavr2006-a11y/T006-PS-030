import csv

def load_subscribers(file_path):
    subscribers = []

    with open(file_path, encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            subscribers.append(row)

    return subscribers
