from math import inf, sqrt

from benchmark.functions.ackley import ackley
from benchmark.functions.bukin_n6 import bukin_n6
from benchmark.functions.rastrigin import rastrigin
from algorithms.physical.universal.simulated_annealing_any_func import search


def benchmark_simulated_annealing(function, bounds, repeat_times=20):
    maximum_iterations = 2000
    maximum_temperature = 100000.0
    temperature_change = 0.98

    results = []
    values = []
    best = {'input': None, 'value': inf}

    for i in range(0, repeat_times):
        result = search(function, bounds, maximum_iterations, maximum_temperature, temperature_change)
        if result['value'] < best['value']:
            best = result
        results.append(result)
        values.append(result['value'])

    mean = sum(values) / repeat_times
    stddev = sqrt(sum([(v - mean) ** 2 for v in values]) / (repeat_times - 1))

    print("Metoda AI: Symulowane wyżarzanie")
    print(f"Funkcja benchmark: {function.__name__}")
    print(f"Optimum: {best}")
    print(f"Wyniki ({repeat_times} powtórzeń): ")
    for result in results:
        print(result)
    print(f"Średnia: {mean}")
    print(f"Odchylenie standardowe: {stddev}")


if __name__ == "__main__":
    benchmark_simulated_annealing(ackley, [[-32, 32], [-32, 32]])
    print()
    benchmark_simulated_annealing(bukin_n6, [[-15, -5], [-3, 3]])
    print()
    benchmark_simulated_annealing(rastrigin, [[-5.12, 5.12], [-5.12, 5.12]])
