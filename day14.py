def calc_a(input):
    grid = create_grid(input)
    count = 0
    for row in grid:
        for bit in row:
            if bit == '1':
                count += 1
    return count


def calc_b(input):
    grid = create_grid(input)
    matrix = []
    for grid_row in grid:
        row = list(map(lambda b: 0 if b == '1' else -1, list(grid_row)))
        matrix.append(row)

    group_number = 1
    for y in range(128):
        for x in range(128):
            size = mark_neighbours(matrix, (y, x), group_number)
            if size > 0:
                group_number += 1
    return group_number - 1


def mark_neighbours(matrix, pos, group_number):
    if 0 <= pos[0] < 128 and 128 > pos[1] >= 0 and matrix[pos[0]][pos[1]] == 0:
        matrix[pos[0]][pos[1]] = group_number
        size = 1
        size += mark_neighbours(matrix, (pos[0] + 1, pos[1]), group_number)
        size += mark_neighbours(matrix, (pos[0] - 1, pos[1]), group_number)
        size += mark_neighbours(matrix, (pos[0], pos[1] + 1), group_number)
        size += mark_neighbours(matrix, (pos[0], pos[1] - 1), group_number)
        return size
    return 0


def create_grid(input):
    grid = []
    for i in range(128):
        kh = knot_hash(input + '-' + str(i))
        row = ''.join(map(lambda x: "{0:04b}".format(int(x, 16)), kh))
        grid.append(row)
    return grid


def knot_hash(input):
    length = 256
    key = list(map(lambda c: ord(c), input)) + [17, 31, 73, 47, 23]
    k_hash = list(range(0, length))
    current_position = 0
    skip_size = 0
    for _ in range(64):
        for knot_length in key:
            start = current_position
            end = current_position + min(knot_length, length)
            if end > length:
                reversed = reverse(k_hash[start:] + k_hash[:(end % length)])
                k_hash = reversed[abs(start - length):] + k_hash[(end % length):start] + reversed[:abs(start - length)]
            else:
                k_hash = k_hash[:start] + reverse(k_hash[start:end]) + k_hash[end:]

            current_position = (current_position + skip_size + knot_length) % length
            skip_size += 1

    a = []

    for i in range(16):
        offset = i * 16
        c = k_hash[offset]
        for j in range(1, 16):
            c = c ^ k_hash[offset + j]
        a.append(c)
    return ''.join('%.2x' % x for x in a)

def reverse(lst):
    lst.reverse()
    return lst

