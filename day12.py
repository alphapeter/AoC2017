def calc_a(input):
    programs = get_programs(input)
    counted_programs = set()
    return count_programs(programs, 0, counted_programs)


def calc_b(input):
    programs = get_programs(input)
    counted_programs = set()
    group_count = 0
    for prg, _ in enumerate(programs):
        if prg not in counted_programs:
            count_programs(programs, prg, counted_programs)
            group_count += 1
    return group_count


def get_programs(input):
    programs = []
    for row in input.split('\n'):
        a = row.split('<->')
        int(a[0])
        links = list(map(lambda link: int(link), a[1].split(',')))
        programs.append(links)
    return programs


def count_programs(programs, program, counted_programs):
    if program in counted_programs:
        return 0

    counted_programs.add(program)

    l_count = 0
    for link in programs[program]:
        l_count += count_programs(programs, link, counted_programs)

    return 1 + l_count
