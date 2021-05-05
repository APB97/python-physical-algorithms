from math import exp
from random import random
from typing import List

from numpy.random.mtrand import randn

from algorithms.physical.universal.simulated_annealing import simulated_annealing
from benchmarking.ConfigurableAlgorithmBase import ConfigurableAlgorithmBase
from randomization.Random import Random
from utilities.Bounds import Bounds


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
        return self.__simulated_annealing(function, bounds)

    def __simulated_annealing(self, function, bounds):
        current = {'input': Random.vector_in_bounds(bounds)}
        current['value'] = function(current['input'])
        temperature, best = self.max_temperature, current
        for i in range(1, self.iterations + 1):
            candidate = self.__create_next(current, function, bounds, 1)
            temperature *= self.temperature_change

            if candidate['value'] < best['value']:
                best = candidate
            if self.__should_accept(candidate, current, temperature):
                current = candidate

        return best

    @staticmethod
    def __create_next(current, function, bounds: List[Bounds], step):
        next_input = [bounds[i].keep_in_bounds(current['input'][i] + step * float(randn(1))) for i in range(len(bounds))]
        next_candidate = {'input': next_input, 'value': function(next_input)}
        return next_candidate

    @staticmethod
    def __should_accept(candidate, current, temperature):
        if candidate['value'] <= current['value']:
            return True
        return exp((current['value'] - candidate['value']) / temperature) > random()
