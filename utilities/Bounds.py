class Bounds:

    def __init__(self, minimum, maximum):
        self.minimum = minimum
        self.maximum = maximum

    def keep_in_bounds(self, value):
        return Bounds.keep_in_bounds(value, self.minimum, self.maximum)

    @staticmethod
    def keep_in_bounds(value, minimum, maximum):
        if value < minimum:
            return minimum
        if value > maximum:
            return maximum
        return value
