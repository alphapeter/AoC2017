start_pattern = """.#.
..#
###"""


def get_matching_rule(pattern, rules):
    variants = []
    current = pattern
    # create rotation + flip variations
    for _x in range(4):
        rotate = list(map(lambda x: ''.join(x), list(zip(*reversed(current)))))
        variants.append(rotate)
        current = rotate

        flip_x = list(map(lambda row: str(row[::-1]), current))
        variants.append(flip_x)

    for r in rules:
        for p in variants:
            rule = r.split('=>')
            match_pattern = rule[0].strip().split('/')
            if p == match_pattern:
                return rule[1].strip().split('/')


def calc_a(input, iterations):
    pattern = start_pattern.split('\n')

    rules = input.split('\n')

    for _ in range(iterations):
        size = len(pattern)
        #print('\n'.join(pattern))
        #print('\n')

        new_pixels = []
        if size % 2 == 0:
            for y in range(2, size + 1, 2):
                row = []
                for x in range(2, size + 1, 2):
                    p = list(map(lambda row: str(row[x-2:x]), pattern[y-2:y]))
                    rule = get_matching_rule(p, rules)
                    row.append(rule)
                new_pixels.append(row)

        elif size % 3 == 0:

            for y in range(3, size + 1, 3):
                row = []
                for x in range(3, size + 1, 3):
                    p = list(map(lambda row: str(row[x-3:x]), pattern[y-3:y]))
                    rule = get_matching_rule(p, rules)
                    row.append(rule)
                new_pixels.append(row)

        # Reconstruct the pattern from the pixels
        new_size = len(new_pixels) * len(new_pixels[0][0])
        pattern = [''] * new_size
        for i, row in enumerate(new_pixels):
            for pixel in row:
                for j, sub_row in enumerate(pixel):
                    offset = (i * len(pixel))
                    pattern[offset+j] = ''.join([pattern[offset+j] + sub_row])


       # print('===================================\n')

    # print('\n'.join(pattern))

    count = 0
    for row in pattern:
        for pixel in row:
            if pixel == '#':
                count += 1

    return count
