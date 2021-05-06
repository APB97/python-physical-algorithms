from random import random, randint
from typing import List

from benchmarking.ConfigurableAlgorithmBase import ConfigurableAlgorithmBase
from randomization.Random import Random
from utilities.Bounds import Bounds


class HarmonySearch(ConfigurableAlgorithmBase):
    def __init__(self, memory_size, factor, consider_rate, adjust_rate, harmony_range, iterations):
        super().__init__(self.__call__)
        self.iterations = iterations
        self.factor = factor
        self.memory_size = memory_size
        self.consider_rate = consider_rate
        self.adjust_rate = adjust_rate
        self.harmony_range = harmony_range

    def __name__(self):
        return "Harmony Search"

    def __call__(self, function, bounds):
        return self.__harmony_search(function, bounds)

    def __harmony_search(self, function, bounds: List[Bounds]):
        memory = self.__init_memory(function, bounds)
        best = memory[0]

        for i in range(self.iterations):
            harmony = self.__create_harmony(bounds, memory)
            harmony['value'] = function(harmony['input'])
            if harmony['value'] < best['value']:
                best = harmony
            memory.append(harmony)
            memory.sort(key=lambda m: m['value'])
            memory.remove(memory[-1])
        return best

    def __init_memory(self, function, bounds: List[Bounds]):
        memory = [self.__create_random_harmony(function, bounds) for _ in range(self.memory_size * self.factor)]
        memory.sort(key=lambda m: m['value'])
        return memory[0:self.memory_size]

    @staticmethod
    def __create_random_harmony(function, bounds: List[Bounds]):
        harmony = {'input': Random.vector_in_bounds(bounds)}
        harmony['value'] = function(harmony['input'])
        return harmony

    def __create_harmony(self, bounds: List[Bounds], memory):
        vector = [i for i in range(len(bounds))]
        for i in vector:
            if random() < self.consider_rate:
                value = memory[randint(0, len(memory) - 1)]['input'][i]
                if random() < self.adjust_rate:
                    value = bounds[i].keep_in_bounds(value + self.harmony_range * Random.from_range(-1, 1))
                vector[i] = value
            else:
                vector[i] = Random.from_range(bounds[i].minimum, bounds[i].maximum)
        return {'input': vector}
