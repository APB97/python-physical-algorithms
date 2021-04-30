from algorithms.physical.universal.simulated_annealing import simulated_annealing
from benchmarking.ConfigurableAlgorithmBase import ConfigurableAlgorithmBase


class SimulatedAnnealing(ConfigurableAlgorithmBase):

    def __init__(self, iterations, max_temperature, temperature_change):
        super().__init__(simulated_annealing)
        self.iterations = iterations
        self.max_temperature = max_temperature
        self.temperature_change = temperature_change

    @property
    def __name__(self):
        return "Simulated Annealing"

    def __call__(self, function, bounds):
        return simulated_annealing(function, bounds, self.iterations, self.max_temperature, self.temperature_change)
