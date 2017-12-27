def calc_a(steps):
    buffer = [0]

    current_position = 0
    for i in range(1, 2018):
        current_position = (current_position + steps) % len(buffer) + 1
        buffer = buffer[:current_position] + [i] + buffer[current_position:]

    return buffer[(current_position + 1) % len(buffer)]


def calc_b(steps):
    # value 0 is always on position 0, therefore we only need to handle the value at position 1
    position_1 = 0

    current_position = 0

    for i in range(1, 50000001):
        current_position = (current_position + steps) % i + 1
        if current_position == 1:
            position_1 = i

    return position_1
