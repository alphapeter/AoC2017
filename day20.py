import math


def calc_a(input):
    particles = []
    for particle_number, row in enumerate(input.split('\n')):
        particles.append(Particle(particle_number, row))

    for _ in range(1000):
        for p in particles:
            p.tick()

    distances = []
    for i, particle in enumerate(particles):
        distances.append((i, particle.manhattan_distance()))

    by_distance = sorted(distances, key=lambda x: x[1])

    return by_distance[0][0]


def calc_b(input):
    particles = []
    for particle_number, row in enumerate(input.split('\n')):
        particles.append(Particle(particle_number, row))

    for _ in range(100):
        for p in particles:
            p.tick()

        to_remove = {}
        for p1 in particles:
            for p2 in particles:
                if p1 != p2 and collide(p1, p2):
                    to_remove[p2.particle_number] = p2

        for p in to_remove.values():
            particles.remove(p)

    return len(particles)


def collide(p1, p2):
    return p1.position[0] == p2.position[0] and p1.position[1] == p2.position[1] and p1.position[2] == p2.position[2]


class Particle:
    def __init__(self, particle_number, row):
        vecs = row.split('>,')
        v1 = list(map(lambda x: int(x), vecs[0].strip().strip('p=<').split(',')))
        v2 = list(map(lambda x: int(x), vecs[1].strip().strip('v=<').split(',')))
        v3 = list(map(lambda x: int(x), vecs[2].strip().strip('a=<').strip('>').split(',')))
        self.position = v1
        self.velocity = v2
        self.acceleration = v3
        self.particle_number = particle_number

    def manhattan_distance(self):
        return abs(self.position[0]) + abs(self.position[1]) + abs(self.position[2])

    def tick(self):
        self.velocity[0] += self.acceleration[0]
        self.velocity[1] += self.acceleration[1]
        self.velocity[2] += self.acceleration[2]

        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]
        self.position[2] += self.velocity[2]

