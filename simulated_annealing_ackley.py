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


def create_next(current, delta_step, lower_limits, upper_limits):
    next1 = {'input': list.copy(current['input'])}

    next1['input'][0] = max(lower_limits[0], min(upper_limits[0], next1['input'][0] + float(randn(1)) * delta_step))
    next1['input'][1] = max(lower_limits[1], min(upper_limits[1], next1['input'][1] + float(randn(1)) * delta_step))

    next1['value'] = ackley(next1['input'])
    return next1


def should_accept(candidate: dict, current: dict, temp):

    if candidate['value'] <= current['value']:
        return True
    return exp((current['value'] - candidate['value']) / temp) > random()


def search_ackley(max_iterations, max_temperature, temp_change, print_progress=False):
    current = {'input': [random_from_range(digits=2, start=-32, end=32),
                         random_from_range(digits=2, start=-32, end=32)]}
    current['value'] = ackley(current['input'])
    temperature, best = max_temperature, current
    for i in range(1, max_iterations + 1):
        candidate = create_next(current, 1, lower_limits=[-32, -32], upper_limits=[32, 32])
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
    best_result = search_ackley(maximum_iterations, maximum_temperature, temperature_change, print_progress=True)
    print("Done.")
    print(f"Best solution: value={best_result['value']}, input={best_result['input']}")
