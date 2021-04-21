from math import inf, sqrt

from extremal_optimization_ackley import search_eo_ackley
from extremal_optimization_bukin_n6 import search_eo_bukin_n6
from extremal_optimization_rastrigin import search_eo_rastrigin


def benchmark_extremal_optimization_ackley(repeat_times=20):
    maximum_iterations = 250

    results = []
    values = []
    best = {'input': None, 'value': inf}

    for i in range(0, repeat_times):
        result = search_eo_ackley(maximum_iterations, tau=1.8)
        if result['value'] < best['value']:
            best = result
        results.append(result)
        values.append(result['value'])

    mean = sum(values) / repeat_times
    stddev = sqrt(sum([(v - mean) ** 2 for v in values]) / (repeat_times - 1))

    print("Metoda AI: Ekstremalna optymalizacja")
    print("Funkcja benchmark: Ackley")
    print(f"Optimum: {best}")
    print(f"Wyniki ({repeat_times} powtórzeń): ")
    for result in results:
        print(result)
    print(f"Średnia: {mean}")
    print(f"Odchylenie standardowe: {stddev}")


def benchmark_extremal_optimization_bukin(repeat_times=20):
    maximum_iterations = 250

    results = []
    values = []
    best = {'input': None, 'value': inf}

    for i in range(0, repeat_times):
        result = search_eo_bukin_n6(maximum_iterations, tau=1.8)
        if result['value'] < best['value']:
            best = result
        results.append(result)
        values.append(result['value'])

    mean = sum(values) / repeat_times
    stddev = sqrt(sum([(v - mean) ** 2 for v in values]) / (repeat_times - 1))

    print("Metoda AI: Ekstremalna optymalizacja")
    print("Funkcja benchmark: Bukin no. 6")
    print(f"Optimum: {best}")
    print(f"Wyniki ({repeat_times} powtórzeń): ")
    for result in results:
        print(result)
    print(f"Średnia: {mean}")
    print(f"Odchylenie standardowe: {stddev}")


def benchmark_extremal_optimization_rastrigin(repeat_times=20):
    maximum_iterations = 250

    results = []
    values = []
    best = {'input': None, 'value': inf}

    for i in range(0, repeat_times):
        result = search_eo_rastrigin(maximum_iterations, tau=1.8)
        if result['value'] < best['value']:
            best = result
        results.append(result)
        values.append(result['value'])

    mean = sum(values) / repeat_times
    stddev = sqrt(sum([(v - mean) ** 2 for v in values]) / (repeat_times - 1))

    print("Metoda AI: Ekstremalna optymalizacja")
    print("Funkcja benchmark: Rastrigin")
    print(f"Optimum: {best}")
    print(f"Wyniki ({repeat_times} powtórzeń): ")
    for result in results:
        print(result)
    print(f"Średnia: {mean}")
    print(f"Odchylenie standardowe: {stddev}")


if __name__ == "__main__":
    benchmark_extremal_optimization_ackley()
    print()
    benchmark_extremal_optimization_bukin()
    print()
    benchmark_extremal_optimization_rastrigin()
