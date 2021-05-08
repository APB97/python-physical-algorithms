from random import randint
from typing import List

from benchmarking.ConfigurableAlgorithmBase import ConfigurableAlgorithmBase
from randomization.Random import Random
from utilities.Bounds import Bounds


class CulturalAlgorithm(ConfigurableAlgorithmBase):
    def __init__(self, pop_size, generations, num_accepted):
        super().__init__(self.__call__)
        self.num_accepted = num_accepted
        self.generations = generations
        self.pop_size = pop_size

    def __name__(self):
        return "Cultural Algorithm"

    def __call__(self, function, bounds):
        return self.__cultural_algorithm(function, bounds)

    def __cultural_algorithm(self, function, bounds):
        population = [{'input': Random.vector_in_bounds(bounds)} for _ in range(self.pop_size)]
        belief_space = self.__init_belief_space(bounds)
        for p in population:
            p['value'] = function(p['input'])
        population.sort(key=lambda pop: pop['value'])
        best = population[0]
        self.__update_belief_space_situational(belief_space, best)
        for g in range(self.generations):
            children = [self.__mutate_with(p, belief_space['normative'], bounds) for p in population]
            for c in children:
                c['value'] = function(c['input'])
            children.sort(key=lambda ch: ch['value'])
            best = children[0]
            self.__update_belief_space_situational(belief_space, best)
            population = [self.__binary_tournament(population + children) for _ in range(self.pop_size)]
            population.sort(key=lambda popul: popul['value'])
            accepted = population[:self.num_accepted]
            self.__update_belief_space_normative(belief_space['normative'], accepted)
        return belief_space['situational']

    @staticmethod
    def __init_belief_space(bounds: List[Bounds]):
        return {'situational': None, 'normative': [Bounds(b.minimum, b.maximum) for b in bounds]}

    @staticmethod
    def __update_belief_space_situational(belief_space, best):
        current_best = belief_space['situational']
        if current_best is None or best['value'] < current_best['value']:
            belief_space['situational'] = best

    @staticmethod
    def __mutate_with(candidate, beliefs_normative: List[Bounds], bounds):
        vector = [0 for _ in range(len(candidate['input']))]
        for i in range(len(candidate['input'])):
            vector[i] = Random.from_range(beliefs_normative[i].minimum, beliefs_normative[i].maximum)
            vector[i] = bounds[i].keep_in_bounds(vector[i])
        return {'input': vector}

    @staticmethod
    def __binary_tournament(pop):
        i, j = randint(0, len(pop) - 1), randint(0, len(pop) - 1)
        while j == i:
            j = randint(0, len(pop) - 1)
        if pop[i]['value'] < pop[j]['value']:
            return pop[i]
        else:
            return pop[j]

    @staticmethod
    def __update_belief_space_normative(beliefs_normative, accepted):
        for i in range(len(beliefs_normative)):
            beliefs_normative[i].minimum = min([a['input'][i] for a in accepted])
            beliefs_normative[i].maximum = max([a['input'][i] for a in accepted])
