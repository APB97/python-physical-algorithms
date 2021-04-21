# Author of the implementation: Adrian Bieliński
from random import random
from numpy.random.mtrand import randn

from ackley import ackley


def calculate_component_probabilities(ordered_components, tau):
    sum_of = 0.0
    for i in range(0, len(ordered_components)):
        ordered_components[i]['prob'] = (i + 1.0) ** (-tau)
        sum_of += ordered_components[i]['prob']
    return sum_of


def make_selection(components, sum_of_probability):
    selection = random()
    for i in range(0, len(components)):
        selection -= components[i]['prob'] / sum_of_probability
        if selection <= 0.0:
            return i
    return len(components) - 1


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


def search_eo_ackley(max_iterations, tau):
    current = {'input': [random_from_range(digits=2, start=-32, end=32),
                         random_from_range(digits=2, start=-32, end=32)]}
    current['value'] = ackley(current['input'])
    best = current

    for i in range(1, max_iterations + 1):

        candidate = {'input': [current['input'][0], current['input'][1]]}

        components = [{'prob': 0}, {'prob': 0}]
        prob_sum = calculate_component_probabilities(components, tau)
        weak_component = make_selection(components, prob_sum)

        candidate['input'][weak_component] = random_from_range(digits=2, start=-32, end=32)

        candidate['value'] = ackley(candidate['input'])
        current = candidate

        if candidate['value'] < best['value']:
            best = candidate

        print(f"Iteration {i}, current_cost={current['value']}, best_cost={best['value']}")
    return best


# algorithm configuration
maximum_iterations = 250
tau_parameter = 1.8  # 4  # 10.75  # 1.8

# algorithm execution
best_result = search_eo_ackley(maximum_iterations, tau_parameter)
print("Done.")
print(f"Best solution: cost={best_result['value']}, vector={best_result['input']}")
