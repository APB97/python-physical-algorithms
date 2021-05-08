# Author of the implementation: Adrian Bieliński
from random import random


def random_from_range(digits, start, end):
    uniform_random = random()
    value_from_range = uniform_random * (end - start) + start
    value_from_range = round(value_from_range, digits)
    return value_from_range


def search(function, bounds, max_iterations, eps=0.1, print_progress=False):
    current = {'input': [random_from_range(2, bounds[i][0], bounds[i][1]) for i in range(len(bounds))]}
    current['value'] = function(current['input'])
    best = current

    for i in range(1, max_iterations + 1):

        candidate = {'input': list.copy(current['input'])}

        fits = [function([candidate['input'][i]]) for i in range(len(bounds))]
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
