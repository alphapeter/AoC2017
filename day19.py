down = 0
right = 1
up = 2
left = 3

moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def calc_a(input):
    return calc(input)[0]


def calc_b(input):
    return calc(input)[1]


def calc(input):
    rows = input.split('\n')

    x = rows[0].index('|')
    y = 0

    direction = down
    letters = []
    steps = 0

    while True:
        path = rows[y][x]
        if path == ' ':
            return ''.join(letters), steps

        elif path == '+':
            if direction == down or direction == up:
                dx = x - 1
                dp = rows[y][dx]
                if dx >= 0 and dp == '-' or 'A' <= dp <= 'Z':
                    x = dx
                    direction = left
                else:
                    x = x + 1
                    direction = right

            else:
                dy = y - 1
                dp = rows[dy][x]
                if dy >= 0 and dp == '|' or 'A' <= dp <= 'Z':
                    y = dy
                    direction = up
                else:
                    y = y + 1
                    direction = down

            steps += 1
            continue

        if 'A' <= path <= 'Z':
            letters.append(path[0])

        y += moves[direction][0]
        x += moves[direction][1]

        steps += 1

        if not (0 <= x < len(rows[0]) and 0 <= y < len(rows)):
            return ''.join(letters), steps
