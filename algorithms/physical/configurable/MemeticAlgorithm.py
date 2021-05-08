from random import randint, random
from typing import List

from benchmarking.ConfigurableAlgorithmBase import ConfigurableAlgorithmBase
from randomization.Random import Random
from utilities.Bounds import Bounds


class MemeticAlgorithm(ConfigurableAlgorithmBase):
    def __init__(self, bits_per_parameter, population_size, generations, max_local_gens, prob_local,
                 prob_cross, prob_mut=None):
        super().__init__(self.__memetic_algorithm)
        self.max_local_gens = max_local_gens
        self.prob_local = prob_local
        self.prob_mut = prob_mut
        self.prob_cross = prob_cross
        self.generations = generations
        self.population_size = population_size
        self.bits_per_parameter = bits_per_parameter

    def __name__(self):
        return "Memetic Algorithm"

    def __call__(self, function, bounds):
        return self.__memetic_algorithm(function, bounds)

    def __memetic_algorithm(self, function, bounds: List[Bounds]):
        total_bits = len(bounds) * self.bits_per_parameter
        population = [{'bits': Random.bits(total_bits)} for _ in range(self.population_size)]
        for c in population:
            self.__fitness(c, function, bounds)
        population.sort(key=lambda p: p['value'])
        generation, best = 0, population[0]
        for i in range(1, self.generations):
            selected = [self.__binary_tournament(population) for _ in range(self.population_size)]
            children = self.__reproduce(selected)
            for c in children:
                self.__fitness(c, function, bounds)
            population = []
            for c in children:
                if random() < self.prob_local:
                    c = self.__bit_climber(c, function, bounds)
                population.append(c)
            population.sort(key=lambda p: p['value'])
            if population[0]['value'] <= best['value']:
                best = population[0]
        return best

    def __fitness(self, candidate, function, bounds: List[Bounds]):
        candidate['input'] = self.__decode(candidate['bits'], bounds, self.bits_per_parameter)
        candidate['value'] = function(candidate['input'])

    @staticmethod
    def __decode(bits, bounds: List[Bounds], bits_per_parameter):
        vector = [0 for _ in range(len(bounds))]
        for i in range(len(bounds)):
            offset, total_sum = i * bits_per_parameter, 0.0
            parameter_bits = list(reversed(bits[offset:offset + bits_per_parameter]))
            total_sum = sum([parameter_bits[j] * 2 ** j for j in range(len(parameter_bits))])
            min_bound, max_bound = bounds[i].minimum, bounds[i].maximum
            vector[i] = min_bound + ((max_bound - min_bound) / ((2 ** bits_per_parameter) - 1.0)) * total_sum
        return vector

    @staticmethod
    def __binary_tournament(pop):
        i, j = randint(0, len(pop) - 1), randint(0, len(pop) - 1)
        while j == i:
            j = randint(0, len(pop) - 1)
        if pop[i]['value'] < pop[j]['value']:
            return pop[i]
        else:
            return pop[j]

    def __reproduce(self, selected):
        children = []
        steps = [1, -1]
        for i in range(len(selected)):
            p2 = selected[i + steps[i % 2]]
            if i == len(selected) - 1:
                p2 = selected[0]
            bitstring = self.__crossover(selected[i]['bits'], p2['bits'])
            bitstring = self.__point_mutation(bitstring)
            children.append({'bits': bitstring})
            if len(children) >= self.population_size:
                break
        return children

    def __crossover(self, parent1, parent2):
        if random() >= self.prob_cross:
            return list(parent1)

        def random_pick(index):
            if random() < 0.5:
                return parent1[index]
            else:
                return parent2[index]

        return [random_pick(i) for i in range(len(parent1))]

    def __point_mutation(self, bitstring):
        rate = self.prob_mut
        if rate is None:
            rate = 1.0 / len(bitstring)

        def consider_negate(bit):
            if random() < rate:
                return self.__negate(bit)
            else:
                return bit

        return [consider_negate(bit) for bit in bitstring]

    @staticmethod
    def __negate(bit):
        if bit == 1:
            return 0
        else:
            return 1

    def __bit_climber(self, c, function, bounds):
        current = c
        for i in range(self.max_local_gens):
            candidate = {'bits': self.__point_mutation(current['bits'])}
            self.__fitness(candidate, function, bounds)
            if candidate['value'] <= current['value']:
                current = candidate
        return current
