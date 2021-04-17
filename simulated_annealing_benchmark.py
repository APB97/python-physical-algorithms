from math import inf, sqrt

from simulated_annealing_ackley import search_ackley
from simulated_annealing_bukin_n6 import search_bukin
from simulated_annealing_rastrigin import search_rastrigin


def benchmark_simulated_annealing_ackley(repeat_times=20):
    maximum_iterations = 2000
    maximum_temperature = 100000.0
    temperature_change = 0.98

    results = []
    values = []
    best = {'input': None, 'value': inf}

    for i in range(0, repeat_times):
        result = search_ackley(maximum_iterations, maximum_temperature, temperature_change)
        if result['value'] < best['value']:
            best = result
        results.append(result)
        values.append(result['value'])

    mean = sum(values) / repeat_times
    stddev = sqrt(sum([(v - mean) ** 2] for v in values) / (repeat_times - 1))

    print("Metoda AI: Symulowane wyżarzanie")
    print("Funkcja benchmark: Ackley")
    print(f"Optimum: {best}")
    print(f"Wyniki ({repeat_times} powtórzeń): ")
    for result in results:
        print(result)
    print(f"Średnia: {mean}")
    print(f"Odchylenie standardowe: {stddev}")


def benchmark_simulated_annealing_bukin(repeat_times=20):
    maximum_iterations = 2000
    maximum_temperature = 100000.0
    temperature_change = 0.98

    results = []
    values = []
    best = {'input': None, 'value': inf}

    for i in range(0, repeat_times):
        result = search_bukin(maximum_iterations, maximum_temperature, temperature_change)
        if result['value'] < best['value']:
            best = result
        results.append(result)
        values.append(result['value'])

    mean = sum(values) / repeat_times
    stddev = sqrt(sum([(v - mean) ** 2] for v in values) / (repeat_times - 1))

    print("Metoda AI: Symulowane wyżarzanie")
    print("Funkcja benchmark: Bukin no. 6")
    print(f"Optimum: {best}")
    print(f"Wyniki ({repeat_times} powtórzeń): ")
    for result in results:
        print(result)
    print(f"Średnia: {mean}")
    print(f"Odchylenie standardowe: {stddev}")


def benchmark_simulated_annealing_rastrigin(repeat_times=20):
    maximum_iterations = 2000
    maximum_temperature = 100000.0
    temperature_change = 0.98

    results = []
    values = []
    best = {'input': None, 'value': inf}

    for i in range(0, repeat_times):
        result = search_rastrigin(maximum_iterations, maximum_temperature, temperature_change)
        if result['value'] < best['value']:
            best = result
        results.append(result)
        values.append(result['value'])

    mean = sum(values) / repeat_times
    stddev = sqrt(sum([(v - mean) ** 2] for v in values) / (repeat_times - 1))

    print("Metoda AI: Symulowane wyżarzanie")
    print("Funkcja benchmark: Rastrigin")
    print(f"Optimum: {best}")
    print(f"Wyniki ({repeat_times} powtórzeń): ")
    for result in results:
        print(result)
    print(f"Średnia: {mean}")
    print(f"Odchylenie standardowe: {stddev}")


if __name__ == "__main__":
    benchmark_simulated_annealing_ackley()
    print()
    benchmark_simulated_annealing_bukin()
    print()
    benchmark_simulated_annealing_rastrigin()
