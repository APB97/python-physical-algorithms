class ConfigurableAlgorithmBase:
    def __init__(self, algorithm):
        self.algorithm = algorithm

    def __call__(self, function, bounds):
        return self.algorithm(function, bounds)
