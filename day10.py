def calc_a(input, length):

    k_hash = list(range(0, length))
    print(k_hash)
    current_position = 0
    skip_size = 0
    for knot_length in input:
        start = current_position
        end = current_position + min(knot_length, length)
        print('start', start, 'end', end)
        if end > length:
            reversed = reverse(k_hash[start:] + k_hash[:(end % length)])
            k_hash = reversed[abs(start - length):] + k_hash[(end % length):start] + reversed[:abs(start - length)]
        else:
            k_hash = k_hash[:start] + reverse(k_hash[start:end]) + k_hash[end:]

        print(k_hash)
        current_position = (current_position + skip_size + knot_length) % length
        skip_size += 1

    return k_hash[0] * k_hash[1]


def reverse(lst):
    lst.reverse()
    return lst

def calc_b(input):
    return 0

