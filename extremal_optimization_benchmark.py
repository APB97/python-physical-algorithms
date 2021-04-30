from math import inf, sqrt

from benchmark.functions.ackley import ackley
from benchmark.functions.bukin_n6 import bukin_n6
from extremal_optimization_any_func import search
from benchmark.functions.rastrigin import rastrigin


def benchmark_extremal_optimization(function, bounds, repeat_times=20):
    maximum_iterations = 250

    results = []
    values = []
    best = {'input': None, 'value': inf}

    for i in range(0, repeat_times):
        result = search(function, bounds, maximum_iterations)
        if result['value'] < best['value']:
            best = result
        results.append(result)
        values.append(result['value'])

    mean = sum(values) / repeat_times
    stddev = sqrt(sum([(v - mean) ** 2 for v in values]) / (repeat_times - 1))

    print("Metoda AI: Ekstremalna optymalizacja")
    print(f"Funkcja benchmark: {function.__name__}")
    print(f"Optimum: {best}")
    print(f"Wyniki ({repeat_times} powtórzeń): ")
    for result in results:
        print(result)
    print(f"Średnia: {mean}")
    print(f"Odchylenie standardowe: {stddev}")


if __name__ == "__main__":
    benchmark_extremal_optimization(ackley, [[-32, 32], [-32, 32]])
    print()
    benchmark_extremal_optimization(bukin_n6, [[-15, -5], [-3, 3]])
    print()
    benchmark_extremal_optimization(rastrigin, [[-5.12, 5.12], [-5.12, 5.12]])
