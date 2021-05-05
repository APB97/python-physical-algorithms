class Bounds:

    def __init__(self, minimum, maximum):
        self.minimum = minimum
        self.maximum = maximum

    def keep_in_bounds(self, value):
        if value < self.minimum:
            return self.minimum
        if value > self.maximum:
            return self.maximum
        return value
