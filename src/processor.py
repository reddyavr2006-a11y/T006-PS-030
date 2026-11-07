def process_command(command):

    parts = command.split("|")

    command_type = parts[0]

    print("Processing:", command_type)
