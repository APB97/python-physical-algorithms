from math import inf, sqrt

from cultural_algorithm_ackley import search_ackley
from cultural_algorithm_bukin_n6 import search_bukin_n6
from cultural_algorithm_rastrigin import search_rastrigin


def benchmark_cultural_algorithm_ackley(repeat_times=20):
    problem_size = 2
    problem_bounds = [[-32, 32] for _ in range(problem_size)]

    # algorithm configuration
    generations = 200
    population_size = 100
    number_accepted = population_size // 5

    results = []
    values = []
    best = {'input': None, 'value': inf}

    for i in range(0, repeat_times):
        result = search_ackley(generations, problem_bounds, population_size, number_accepted)
        if result['value'] < best['value']:
            best = result
        results.append(result)
        values.append(result['value'])

    mean = sum(values) / repeat_times
    stddev = sqrt(sum([(v - mean) ** 2 for v in values]) / (repeat_times - 1))

    print("Metoda AI: Algorytm kulturowy")
    print("Funkcja benchmark: Ackley")
    print(f"Optimum: {best}")
    print(f"Wyniki ({repeat_times} powtórzeń): ")
    for result in results:
        print(result)
    print(f"Średnia: {mean}")
    print(f"Odchylenie standardowe: {stddev}")


def benchmark_cultural_algorithm_bukin(repeat_times=20):
    problem_bounds = [[-15, -5], [-3, 3]]

    # algorithm configuration
    generations = 200
    population_size = 100
    number_accepted = population_size // 5

    results = []
    values = []
    best = {'input': None, 'value': inf}

    for i in range(0, repeat_times):
        result = search_bukin_n6(generations, problem_bounds, population_size, number_accepted)
        if result['value'] < best['value']:
            best = result
        results.append(result)
        values.append(result['value'])

    mean = sum(values) / repeat_times
    stddev = sqrt(sum([(v - mean) ** 2 for v in values]) / (repeat_times - 1))

    print("Metoda AI: Algorytm kulturowy")
    print("Funkcja benchmark: Bukin no. 6")
    print(f"Optimum: {best}")
    print(f"Wyniki ({repeat_times} powtórzeń): ")
    for result in results:
        print(result)
    print(f"Średnia: {mean}")
    print(f"Odchylenie standardowe: {stddev}")


def benchmark_cultural_algorithm_rastrigin(repeat_times=20):
    problem_size = 2
    problem_bounds = [[-5.12, 5.12] for _ in range(problem_size)]

    # algorithm configuration
    generations = 200
    population_size = 100
    number_accepted = population_size // 5

    results = []
    values = []
    best = {'input': None, 'value': inf}

    for i in range(0, repeat_times):
        result = search_rastrigin(generations, problem_bounds, population_size, number_accepted)
        if result['value'] < best['value']:
            best = result
        results.append(result)
        values.append(result['value'])

    mean = sum(values) / repeat_times
    stddev = sqrt(sum([(v - mean) ** 2 for v in values]) / (repeat_times - 1))

    print("Metoda AI: Algorytm kulturowy")
    print("Funkcja benchmark: Rastrigin")
    print(f"Optimum: {best}")
    print(f"Wyniki ({repeat_times} powtórzeń): ")
    for result in results:
        print(result)
    print(f"Średnia: {mean}")
    print(f"Odchylenie standardowe: {stddev}")


if __name__ == "__main__":
    benchmark_cultural_algorithm_ackley()
    print()
    benchmark_cultural_algorithm_bukin()
    print()
    benchmark_cultural_algorithm_rastrigin()
