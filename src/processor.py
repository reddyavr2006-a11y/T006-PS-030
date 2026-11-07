def process_command(command):

    parts = command.split("|")

    command_type = parts[0]

    print(f"Command Type: {command_type}")

    if command_type == "CONTRIBUTE":
        contribution_id = parts[1]
        subscriber_id = parts[2]
        tier = parts[3]
        date_time = parts[4]
        contribution_type = parts[5]
        amount = parts[6]

        print("  Contribution ID:", contribution_id)
        print("  Subscriber:", subscriber_id)
        print("  Tier:", tier)
        print("  Amount:", amount)
