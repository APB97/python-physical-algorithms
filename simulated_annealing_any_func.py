# Author of the implementation: Adrian Bieliński
from math import exp
from random import random

from numpy.random.mtrand import randn

from ackley import ackley


def random_from_range(digits, start, end):
    uniform_random = random()
    value_from_range = uniform_random * (end - start) + start
    value_from_range = round(value_from_range, digits)
    return value_from_range


def create_next(function, current, delta_step, bounds):
    next1 = {'input': list.copy(current['input'])}
    next1['input'] = [max(bounds[i][0], min(bounds[i][1], next1['input'][i] + float(randn(1)) * delta_step))
                      for i in range(len(bounds))]
    next1['value'] = function(next1['input'])
    return next1


def should_accept(candidate: dict, current: dict, temp):

    if candidate['value'] <= current['value']:
        return True
    return exp((current['value'] - candidate['value']) / temp) > random()


def search(function, bounds, max_iterations, max_temperature, temp_change, print_progress=False):
    current = {'input': [random_from_range(2, bounds[i][0], bounds[i][1]) for i in range(len(bounds))]}
    current['value'] = function(current['input'])
    temperature, best = max_temperature, current
    for i in range(1, max_iterations + 1):
        candidate = create_next(function, current, 1, bounds)
        temperature = temperature * temp_change

        if candidate['value'] < best['value']:
            best = candidate

        if should_accept(candidate, current, temperature):
            current = candidate

        if print_progress and i % 10 == 0:
            print(f"iteration {i}, temperature={temperature}, best={best['value']}")

    return best


if __name__ == "__main__":
    # algorithm configuration
    maximum_iterations = 2000
    maximum_temperature = 100000.0
    temperature_change = 0.98

    # algorithm execution
    best_result = search(ackley, [[-32, 32], [-32, 32]],
                         maximum_iterations, maximum_temperature, temperature_change, print_progress=True)
    print("Done.")
    print(f"Best solution: value={best_result['value']}, input={best_result['input']}")
