from math import inf, sqrt

from harmony_search_ackley import search_ackley
from harmony_search_bukin_n6 import search_bukin_n6
from harmony_search_rastrigin import search_rastrigin


def benchmark_harmony_search_ackley(repeat_times=20):
    problem_size = 2
    problem_bounds = [[-32, 32] for _ in range(problem_size)]

    # algorithm configuration
    mem = 20
    consider = 0.95
    adjust = 0.7
    harmony_range = 0.05
    iters = 500

    results = []
    values = []
    best = {'input': None, 'value': inf}

    for i in range(0, repeat_times):
        result = search_ackley(problem_bounds, iters, mem, consider, adjust, harmony_range)
        if result['value'] < best['value']:
            best = result
        results.append(result)
        values.append(result['value'])

    mean = sum(values) / repeat_times
    stddev = sqrt(sum([(v - mean) ** 2 for v in values]) / (repeat_times - 1))

    print("Metoda AI: Poszukiwanie harmonii")
    print("Funkcja benchmark: Ackley")
    print(f"Optimum: {best}")
    print(f"Wyniki ({repeat_times} powtórzeń): ")
    for result in results:
        print(result)
    print(f"Średnia: {mean}")
    print(f"Odchylenie standardowe: {stddev}")


def benchmark_harmony_search_bukin(repeat_times=20):
    problem_bounds = [[-15, -5], [-3, 3]]

    # algorithm configuration
    mem = 20
    consider = 0.95
    adjust = 0.7
    harmony_range = 0.05
    iters = 500

    results = []
    values = []
    best = {'input': None, 'value': inf}

    for i in range(0, repeat_times):
        result = search_bukin_n6(problem_bounds, iters, mem, consider, adjust, harmony_range)
        if result['value'] < best['value']:
            best = result
        results.append(result)
        values.append(result['value'])

    mean = sum(values) / repeat_times
    stddev = sqrt(sum([(v - mean) ** 2 for v in values]) / (repeat_times - 1))

    print("Metoda AI: Poszukiwanie harmonii")
    print("Funkcja benchmark: Bukin no. 6")
    print(f"Optimum: {best}")
    print(f"Wyniki ({repeat_times} powtórzeń): ")
    for result in results:
        print(result)
    print(f"Średnia: {mean}")
    print(f"Odchylenie standardowe: {stddev}")


def benchmark_harmony_search_rastrigin(repeat_times=20):
    problem_size = 2
    problem_bounds = [[-5.12, 5.12] for _ in range(problem_size)]

    # algorithm configuration
    mem = 20
    consider = 0.95
    adjust = 0.7
    harmony_range = 0.05
    iters = 500

    results = []
    values = []
    best = {'input': None, 'value': inf}

    for i in range(0, repeat_times):
        result = search_rastrigin(problem_bounds, iters, mem, consider, adjust, harmony_range)
        if result['value'] < best['value']:
            best = result
        results.append(result)
        values.append(result['value'])

    mean = sum(values) / repeat_times
    stddev = sqrt(sum([(v - mean) ** 2 for v in values]) / (repeat_times - 1))

    print("Metoda AI: Poszukiwanie harmonii")
    print("Funkcja benchmark: Rastrigin")
    print(f"Optimum: {best}")
    print(f"Wyniki ({repeat_times} powtórzeń): ")
    for result in results:
        print(result)
    print(f"Średnia: {mean}")
    print(f"Odchylenie standardowe: {stddev}")


if __name__ == "__main__":
    benchmark_harmony_search_ackley()
    print()
    benchmark_harmony_search_bukin()
    print()
    benchmark_harmony_search_rastrigin()
