# Author of the implementation: Adrian Bieliński
from random import random

from rastrigin import rastrigin


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


def search_eo_rastrigin(max_iterations, tau, print_progress=False):
    lower_limits = [-5.12, -5.12]
    upper_limits = [5.12, 5.12]

    current = {'input': [random_from_range(digits=2, start=lower_limits[0], end=upper_limits[0]),
                         random_from_range(digits=2, start=lower_limits[1], end=upper_limits[1])]}
    current['value'] = rastrigin(current['input'])
    best = current

    for i in range(1, max_iterations + 1):

        candidate = {'input': [current['input'][0], current['input'][1]]}

        components = [{'prob': 0}, {'prob': 0}]
        prob_sum = calculate_component_probabilities(components, tau)
        weak_component = make_selection(components, prob_sum)

        candidate['input'][weak_component] = random_from_range(digits=2, start=lower_limits[weak_component],
                                                               end=upper_limits[weak_component])

        candidate['value'] = rastrigin(candidate['input'])
        current = candidate

        if candidate['value'] < best['value']:
            best = candidate

        if print_progress:
            print(f"Iteration {i}, current_value={current['value']}, best_value={best['value']}")
    return best


if __name__ == "__main__":
    # algorithm configuration
    maximum_iterations = 250
    tau_parameter = 1.8

    # algorithm execution
    best_result = search_eo_rastrigin(maximum_iterations, tau_parameter, print_progress=True)
    print("Done.")
    print(f"Best solution: value={best_result['value']}, input={best_result['input']}")
