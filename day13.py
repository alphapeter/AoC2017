def calc_a(input):
    scanned_layers = create_layers(input)

    severity = 0

    for tick, layer in scanned_layers.items():
        if layer.is_detected(tick):
            severity += tick * layer.range

    return severity


def calc_b(input):
    scanned_layers = create_layers(input)
    max_layer = max(scanned_layers.keys())
    delay = 0
    while True:
        for ticks, layer in scanned_layers.items():
            if layer.is_detected(ticks + delay):
                break
            if ticks >= max_layer:
                return delay
        delay += 1
    return delay


def create_layers(input):
    scanned_layers = {}
    for row in input.split('\n'):
        tokens = row.split(':')

        layer_range = int(tokens[1])
        layer = int(tokens[0])
        scanned_layers[layer] = Layer(layer_range)
    return scanned_layers


class Layer:
    def __init__(self, range):
        self.range = range
        self.scanner_range = range * 2 - 2

    def is_detected(self, ticks):
        return ticks % self.scanner_range == 0
