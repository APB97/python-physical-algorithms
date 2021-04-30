from math import inf, sqrt

from benchmark.functions.ackley import ackley
from benchmark.functions.bukin_n6 import bukin_n6
from algorithms.physical.universal.harmony_search import search
from benchmark.functions.rastrigin import rastrigin


def benchmark_harmony_search(function, bounds, repeat_times=20):
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
        result = search(function, bounds, iters, mem, consider, adjust, harmony_range)
        if result['value'] < best['value']:
            best = result
        results.append(result)
        values.append(result['value'])

    mean = sum(values) / repeat_times
    stddev = sqrt(sum([(v - mean) ** 2 for v in values]) / (repeat_times - 1))

    print("Metoda AI: Poszukiwanie harmonii")
    print(f"Funkcja benchmark: {function.__name__}")
    print(f"Optimum: {best}")
    print(f"Wyniki ({repeat_times} powtórzeń): ")
    for result in results:
        print(result)
    print(f"Średnia: {mean}")
    print(f"Odchylenie standardowe: {stddev}")


if __name__ == "__main__":
    benchmark_harmony_search(ackley, [[-32, 32], [-32, 32]])
    print()
    benchmark_harmony_search(bukin_n6, [[-15, -5], [-3, 3]])
    print()
    benchmark_harmony_search(rastrigin, [[-5.12, 5.12], [-5.12, 5.12]])
