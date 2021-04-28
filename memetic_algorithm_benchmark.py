from math import inf, sqrt

from ackley import ackley
from bukin_n6 import bukin_n6
from memetic_algorithm_any_func import search
from rastrigin import rastrigin


def benchmark_memetic_algorithm(function, problem_bounds, repeat_times=20):
    # algorithm configuration
    generations = 32
    population_size = 100
    prob_cross = 0.98
    prob_mut = 1.0 / (len(problem_bounds) * 16)
    max_local_generations = 20
    prob_local = 0.5

    results = []
    values = []
    best = {'input': None, 'value': inf}

    for i in range(0, repeat_times):
        result = search(function, generations, problem_bounds, population_size, prob_cross, prob_mut,
                        max_local_generations, prob_local)
        if result['value'] < best['value']:
            best = result
        results.append(result)
        values.append(result['value'])

    mean = sum(values) / repeat_times
    stddev = sqrt(sum([(v - mean) ** 2 for v in values]) / (repeat_times - 1))

    print("Metoda AI: Algorytm memetyczny")
    print(f"Funkcja benchmark: {function.__name__}")
    best['bits'] = ''.join([str(b) for b in best['bits']])
    print(f"Optimum: {best}")
    print(f"Wyniki ({repeat_times} powtórzeń): ")
    for result in results:
        result['bits'] = ''.join([str(b) for b in result['bits']])
        print(result)
    print(f"Średnia: {mean}")
    print(f"Odchylenie standardowe: {stddev}")


if __name__ == "__main__":
    benchmark_memetic_algorithm(ackley, [[-32, 32], [-32, 32]])
    print()
    benchmark_memetic_algorithm(bukin_n6, [[-15, -5], [-3, 3]])
    print()
    benchmark_memetic_algorithm(rastrigin, [[-5.12, 5.12], [-5.12, 5.12]])
