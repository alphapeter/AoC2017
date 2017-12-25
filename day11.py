def calc_a(input):
    distance, _ = calc(input)
    return distance


def calc_b(input):
    _, max_distance = calc(input)
    return max_distance


def calc(input):
    position = (0, 0)
    max_distance = 0
    for move in input.split(','):
        if move == 'n':
            position = (position[0], position[1] + 2)
        elif move == 'ne':
            position = (position[0] + 1, position[1] + 1)
        elif move == 'se':
            position = (position[0] + 1, position[1] - 1)
        elif move == 's':
            position = (position[0], position[1] - 2)
        elif move == 'sw':
            position = (position[0] - 1, position[1] - 1)
        elif move == 'nw':
            position = (position[0] - 1, position[1] + 1)

        distance = get_distance(position)
        if distance > max_distance:
            max_distance = distance

    return get_distance(position), max_distance


def get_distance(position):
    x = position[0]
    y = position[1]
    if abs(y) > abs(x):
        return (abs(y) - abs(x)) // 2 + abs(x)
    return abs(x)
