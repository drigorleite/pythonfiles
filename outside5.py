def decode(message_file):
    with open(message_file, 'r') as file:
        lines = file.readlines()

    # Parse each line and store as tuple (number, word) in a list
    items = []
    for line in lines:
        parts = line.strip().split()  # Strip whitespace and split by spaces
        if len(parts) == 2:  # Ensure there are exactly two parts
            try:
                num = int(parts[0])
                word = parts[1]
                items.append((num, word))
            except ValueError:
                print(f"Skipping invalid line: {line.strip()}")
        else:
            print(f"Skipping invalid line: {line.strip()}")

    # Sort items by the number to ensure the correct order
    items.sort()

    # Extract the words based on the pyramid structure
    step = 1
    index = 0
    result = []

    while index < len(items):
        # Move index to the last item of the current pyramid row
        if index + step <= len(items):
            result.append(items[index + step - 1][1])
        index += step
        step += 1

    return " ".join(result)


# Example usage (assuming the message is stored in 'message.txt'):
decoded_message = decode('message.txt')
print(decoded_message)
