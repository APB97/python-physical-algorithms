# Author of the implementation: Adrian Bieliński
from random import random

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


def search_eo_ackley(function, max_iterations, eps=0.1, print_progress=False):
    bounds = [[-32, 32] for _ in range(2)]
    current = {'input': [random_from_range(2, bounds[i][0], bounds[i][1]) for i in range(2)]}
    current['value'] = function(current['input'])
    best = current

    for i in range(1, max_iterations + 1):

        candidate = {'input': list.copy(current['input'])}

        fits = [function([candidate['input'][i]]) for i in range(2)]
        bestc = fits.index(min(fits))
        worst = fits.index(max(fits))
        distmax = max([abs(x - y) for x in candidate['input'] for y in candidate['input']])
        u = random_from_range(2, -1, 1)
        if distmax < eps:
            distmax = bounds[0][1] - bounds[0][0] / 4  # experimental value

        comp_new = candidate['input'][bestc] + distmax * u
        candidate['input'][worst] = comp_new

        candidate['value'] = function(candidate['input'])
        current = candidate

        if candidate['value'] < best['value']:
            best = candidate

        if print_progress:
            print(f"Iteration {i}, current_value={current['value']}, best_value={best['value']}, in={best['input']}")
    return best


if __name__ == "__main__":
    # algorithm configuration
    maximum_iterations = 250
    tau_parameter = 1.8

    # algorithm execution
    best_result = search_eo_ackley(ackley, maximum_iterations, print_progress=True)
    print("Done.")
    print(f"Best solution: value={best_result['value']}, input={best_result['input']}")
