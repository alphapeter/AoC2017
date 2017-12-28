down = 0
left = 1
up = 2
right = 3


def calc_a(input):
    rows = input.split('\n')
    width = len(rows[0])
    height = len(rows)

    infected_nodes = set()

    for y, row in enumerate(rows):
        for x, node in enumerate(row):
            if node == '#':
                infected_nodes.add((x - width // 2, y - height // 2))

    direction = up
    position = (0, 0)
    infection_bursts = 0

    for _ in range(10000):
        if position in infected_nodes:
            direction = turn_right(direction)
            infected_nodes.remove(position)
        else:
            direction = turn_left(direction)
            infected_nodes.add(position)
            infection_bursts += 1
        position = move_forward(position, direction)

    return infection_bursts


Weakened = 0
Infected = 1
Flagged = 2


def calc_b(input):
    rows = input.split('\n')
    width = len(rows[0])
    height = len(rows)

    infected_nodes = {}

    for y, row in enumerate(rows):
        for x, node in enumerate(row):
            if node == '#':
                infected_nodes[(x - width // 2, y - height // 2)] = Infected

    direction = up
    position = (0, 0)
    infection_bursts = 0

    for _ in range(10000000):
        if position not in infected_nodes:
            direction = turn_left(direction)
            infected_nodes[position] = Weakened

        elif infected_nodes[position] == Weakened:
            infected_nodes[position] = Infected
            infection_bursts += 1

        elif infected_nodes[position] == Infected:
            direction = turn_right(direction)
            infected_nodes[position] = Flagged

        elif infected_nodes[position] == Flagged:
            direction = reverse_direction(direction)

            del infected_nodes[position]
        position = move_forward(position, direction)

    return infection_bursts


def move_forward(position, direction):
    if direction == down:
        return position[0], position[1] + 1
    elif direction == up:
        return position[0], position[1] - 1
    elif direction == left:
        return position[0] - 1, position[1]
    elif direction == right:
        return position[0] + 1, position[1]


def reverse_direction(direction):
    direction = turn_right(direction)
    return turn_right(direction)


def turn_right(direction):
    return (direction + 1) % 4


def turn_left(direction):
    if direction == 0:
        return 3
    return direction - 1
