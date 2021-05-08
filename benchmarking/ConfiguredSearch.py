class ConfiguredSearch:
    def __init__(self, algorithm, function, bounds):
        self.function = function
        self.algorithm = algorithm
        self.bounds = bounds

    def search(self):
        return self.algorithm(self.function, self.bounds)

    def algorithm_name(self):
        return self.algorithm.__name__

    def benchmark_name(self):
        return self.function.__name__
