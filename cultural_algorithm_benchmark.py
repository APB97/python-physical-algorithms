from math import inf, sqrt

from benchmark.functions.ackley import ackley
from benchmark.functions.bukin_n6 import bukin_n6
from algorithms.physical.universal.cultural_algorithm_any_func import search
from benchmark.functions.rastrigin import rastrigin


def benchmark_cultural_algorithm(function, problem_bounds, repeat_times=20):
    # algorithm configuration
    generations = 200
    population_size = 100
    number_accepted = population_size // 5

    results = []
    values = []
    best = {'input': None, 'value': inf}

    for i in range(0, repeat_times):
        result = search(function, generations, problem_bounds, population_size, number_accepted)
        if result['value'] < best['value']:
            best = result
        results.append(result)
        values.append(result['value'])

    mean = sum(values) / repeat_times
    stddev = sqrt(sum([(v - mean) ** 2 for v in values]) / (repeat_times - 1))

    print("Metoda AI: Algorytm kulturowy")
    print(f"Funkcja benchmark: {function.__name__}")
    print(f"Optimum: {best}")
    print(f"Wyniki ({repeat_times} powtórzeń): ")
    for result in results:
        print(result)
    print(f"Średnia: {mean}")
    print(f"Odchylenie standardowe: {stddev}")


if __name__ == "__main__":
    benchmark_cultural_algorithm(ackley, [[-32, 32], [-32, 32]])
    print()
    benchmark_cultural_algorithm(bukin_n6, [[-15, -5], [-3, 3]])
    print()
    benchmark_cultural_algorithm(rastrigin, [[-5.12, 5.12], [-5.12, 5.12]])
