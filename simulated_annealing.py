# Author of the implementation: Adrian Bieliński
from math import sqrt, exp
from operator import contains
from random import randint, random

from typing import List


# euclidean distance
def euclidean_2d(p1, p2):
    return round(sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2))


def cost(permutation: List[int], cities):
    distance = 0

    for i in range(0, len(permutation)):
        if i == len(permutation) - 1:
            city2 = permutation[0]
        else:
            city2 = permutation[i + 1]
        distance += euclidean_2d(cities[permutation[i]], cities[city2])

    return distance


def random_permutation(cities: list):
    permutation = list(range(len(cities)))

    for i in range(0, len(cities)):
        r = randint(0, len(permutation) - 1 - i) + i
        permutation[r], permutation[i] = permutation[i], permutation[r]

    return permutation


def stochastic_two_opt(permutation: List[int]):

    city1, city2 = randint(0, len(permutation) - 1), randint(0, len(permutation) - 1)

    exclude = [city1]
    if city1 == 0:
        exclude.append(len(permutation) - 1)
    else:
        exclude.append(city1 - 1)
    if city1 == len(permutation) - 1:
        exclude.append(0)
    else:
        exclude.append(city1 + 1)

    while contains(exclude, city2):
        city2 = randint(0, len(permutation) - 1)

    if city2 < city1:
        city1, city2 = city2, city1

    reversed_range = permutation[city1:city2]
    reversed_range.reverse()
    for i in range(0, city2 - city1):
        permutation[city1 + i] = reversed_range[i]

    return permutation


def create_neighbor(current: dict, cities):
    candidate = {'vector': list.copy(current['vector'])}
    stochastic_two_opt(candidate['vector'])
    candidate['cost'] = cost(candidate['vector'], cities)
    return candidate


def should_accept(candidate: dict, current: dict, temp):

    if candidate['cost'] <= current['cost']:
        return True
    return exp((current['cost'] - candidate['cost']) / temp) > random()


def search(cities, max_iterations, max_temperature, temp_change):
    current = {'vector': random_permutation(cities)}
    current['cost'] = cost(current['vector'], cities)
    temperature, best = max_temperature, current
    for i in range(1, max_iterations + 1):
        candidate = create_neighbor(current, cities)
        temperature = temperature * temp_change

        if should_accept(candidate, current, temperature):
            current = candidate

        if candidate['cost'] < best['cost']:
            best = candidate

        if i % 10 == 0:
            print(f"iteration {i}, temperature={temperature}, best={best['cost']}")

    return best


# problem definition
berlin52 = [[565, 575], [25, 185], [345, 750], [945, 685], [845, 655],
            [880, 660], [25, 230], [525, 1000], [580, 1175], [650, 1130], [1605, 620],
            [1220, 580], [1465, 200], [1530, 5], [845, 680], [725, 370], [145, 665],
            [415, 635], [510, 875], [560, 365], [300, 465], [520, 585], [480, 415],
            [835, 625], [975, 580], [1215, 245], [1320, 315], [1250, 400], [660, 180],
            [410, 250], [420, 555], [575, 665], [1150, 1160], [700, 580], [685, 595],
            [685, 610], [770, 610], [795, 645], [720, 635], [760, 650], [475, 960],
            [95, 260], [875, 920], [700, 500], [555, 815], [830, 485], [1170, 65],
            [830, 610], [605, 625], [595, 360], [1340, 725], [1740, 245]]

# algorithm configuration
maximum_iterations = 2000
maximum_temperature = 100000.0
temperature_change = 0.98

# algorithm execution
best_result = search(berlin52, maximum_iterations, maximum_temperature, temperature_change)
print("Done.")
print(f"Best solution: cost={best_result['cost']}, vector={best_result['vector']}")
