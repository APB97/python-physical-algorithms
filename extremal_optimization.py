# Author of the implementation: Adrian Bieliński
from math import sqrt
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


def calculate_neighbor_rank(city_number, cities: list, ignore=None):
    if ignore is None:
        ignore = []
    neighbors = []
    for i in range(0, len(cities)):
        if i == city_number or contains(ignore, i):
            continue
        neighbor = {'number': i, 'distance': euclidean_2d(cities[city_number], cities[i])}
        neighbors.append(neighbor)

    def dist(e):
        return e['distance']

    neighbors.sort(key=dist)
    return neighbors


def get_edges_for_city(city_number, perm):
    city1, city2 = None, None
    for i in range(0, len(perm)):
        if perm[i] == city_number:
            city1 = perm[(i - 1) % len(perm)]
            city2 = perm[(i + 1) % len(perm)]
    return [city1, city2]


def calculate_city_fitness(permutation, city_number, cities):
    city1, city2 = get_edges_for_city(city_number, permutation)
    neighbors = calculate_neighbor_rank(city_number, cities)
    n1, n2 = -1, -1
    for i in range(0, len(neighbors)):
        if neighbors[i]['number'] == city1:
            n1 = i + 1
        if neighbors[i]['number'] == city2:
            n2 = i + 1
        if n1 != -1 and n2 != -1:
            break
    return 3.0 / (n1 + n2)


def calculate_city_fitnesses(cities: list, perm):
    city_fitnesses = []
    for i in range(0, len(cities)):
        city_fitness = {'number': i, 'fitness': calculate_city_fitness(perm, i, cities)}
        city_fitnesses.append(city_fitness)

    def fit(e):
        return e['fitness']

    city_fitnesses.sort(key=fit)
    city_fitnesses.reverse()
    return city_fitnesses


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
            return components[i]['number']
    return components[len(components) - 1]['number']


def probabilistic_selection(ordered_components, tau, exclude=None):
    if exclude is None:
        exclude = []
    sum_of = calculate_component_probabilities(ordered_components, tau)
    selected_city = make_selection(ordered_components, sum_of)
    while contains(exclude, selected_city):
        selected_city = make_selection(ordered_components, sum_of)
    return selected_city


def vary_permutation(permutation, selected, new, long_edge):
    perm = list(permutation)
    city1, city2 = None, None  # last indexOf(perm, selected), last indexOf(perm, new)
    for i in range(0, len(perm)):
        if perm[i] == selected:
            city1 = i
        if perm[i] == new:
            city2 = i
    if city1 < city2:
        p1, p2 = city1, city2
    else:
        p1, p2 = city2, city1
    right = (city1 + 1) % len(perm)
    if perm[right] == long_edge:
        reversed_range = perm[p1 + 1:p2]
        reversed_range.reverse()
        for i in range(0, p2 - p1 - 1):
            perm[p1 + 1 + i] = reversed_range[i]
    else:
        reversed_range = perm[p1:p2]
        reversed_range.reverse()
        for i in range(0, p2 - p1):
            perm[p1 + i] = reversed_range[i]
    return perm


def get_long_edge(edges, neighbor_distances: list):
    n1, n2 = None, None
    for i in range(0, len(neighbor_distances)):
        if n1 is None and neighbor_distances[i]['number'] == edges[0]:
            n1 = neighbor_distances[i]
        if n2 is None and neighbor_distances[i]['number'] == edges[1]:
            n2 = neighbor_distances[i]
    if n1['distance'] > n2['distance']:
        return n1['number']
    else:
        return n2['number']


def create_new_perm(cities, tau, perm):
    city_fitnesses = calculate_city_fitnesses(cities, perm)
    city_fitnesses.reverse()
    selected_city = probabilistic_selection(city_fitnesses, tau)
    edges = get_edges_for_city(selected_city, perm)
    neighbors = calculate_neighbor_rank(selected_city, cities)
    new_neighbor = probabilistic_selection(neighbors, tau, edges)
    long_edge = get_long_edge(edges, neighbors)
    return vary_permutation(perm, selected_city, new_neighbor, long_edge)


def search(cities, max_iterations, tau):
    current = {'vector': random_permutation(cities)}
    current['cost'] = cost(current['vector'], cities)
    best = current
    for i in range(1, max_iterations + 1):
        candidate = {'vector': create_new_perm(cities, tau, current['vector'])}
        candidate['cost'] = cost(candidate['vector'], cities)
        current = candidate
        if candidate['cost'] < best['cost']:
            best = candidate
        print(f"Iteration {i}, current_cost={current['cost']}, best_cost={best['cost']}")
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
maximum_iterations = 250
tau_parameter = 1.8

# algorithm execution
best_result = search(berlin52, maximum_iterations, tau_parameter)
print("Done.")
print(f"Best solution: cost={best_result['cost']}, vector={best_result['vector']}")
