def calc_a(input):
    components, start_components = get_components(input)
    max_strength = 0

    for i, component in enumerate(start_components):

        strength = find_max_strength(component, components)
        if strength > max_strength:
            max_strength = strength

    return max_strength


def calc_b(input):
    components, start_components = get_components(input)
    max_length = 0
    max_strength = 0

    for i, component in enumerate(start_components):

        length, strength = find_max_length(component, components)
        if length > max_length or length == max_length and strength > max_strength:
            max_length = length
            max_strength = strength

    return max_strength


def find_max_strength(current, components):
    current_strength = current[0] + current[1]
    max_strength = current_strength

    for i, component in enumerate(components):
        rest_components = components[:i] + components[i + 1:]

        reversed_component = (component[1], component[0])
        for variant in [component, reversed_component]:
            if current[1] == variant[0]:

                total_strength = current_strength + find_max_strength(variant, rest_components)

                if total_strength > max_strength:
                    max_strength = total_strength

    return max_strength


def find_max_length(current, components):
    current_strength = current[0] + current[1]
    max_strength = current_strength

    current_length = 1
    max_length = 1

    for i, component in enumerate(components):
        rest_components = components[:i] + components[i + 1:]

        reversed_component = (component[1], component[0])
        for variant in [component, reversed_component]:
            if current[1] == variant[0]:
                length, strength = find_max_length(variant, rest_components)
                total_strength = current_strength + strength
                total_length = current_length + length
                if total_length > max_length or (total_length == max_length and total_strength > max_strength):
                    max_length = total_length
                    max_strength = total_strength

    return max_length, max_strength


def get_components(input):
    components = []
    start_components = []
    for row in input.split('\n'):
        ports = row.split('/')
        p1 = int(ports[0])
        p2 = int(ports[1])
        if p1 == 0:
            start_components.append((p1, p2))
        elif p2 == 0:
            start_components.append((p2, p1))
        else:
            components.append((p1, p2))
    return components, start_components

