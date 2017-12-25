import binascii
def calc_a(input, length):

    k_hash = list(range(0, length))
    print(k_hash)
    current_position = 0
    skip_size = 0
    for knot_length in input:
        start = current_position
        end = current_position + min(knot_length, length)
        if end > length:
            reversed = reverse(k_hash[start:] + k_hash[:(end % length)])
            k_hash = reversed[abs(start - length):] + k_hash[(end % length):start] + reversed[:abs(start - length)]
        else:
            k_hash = k_hash[:start] + reverse(k_hash[start:end]) + k_hash[end:]

        current_position = (current_position + skip_size + knot_length) % length
        skip_size += 1

    return k_hash[0] * k_hash[1]


def reverse(lst):
    lst.reverse()
    return lst

def calc_b(input, length):

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


