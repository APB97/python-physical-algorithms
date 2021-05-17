from math import inf, sqrt

from benchmarking.ConfigurableAlgorithmBase import ConfigurableAlgorithmBase


def benchmark(algorithm: ConfigurableAlgorithmBase, benchmark_function, bounds, repeat_times=20):
    results = []
    values = []
    best = {'input': None, 'value': inf}

    for i in range(repeat_times):
        result = algorithm(benchmark_function, bounds)
        if result['value'] < best['value']:
            best = result
        results.append(result)
        values.append(result['value'])

    mean = sum(values) / repeat_times
    stddev = sqrt(sum([(v - mean) ** 2 for v in values]) / (repeat_times - 1))

    return {
        'algorithm': algorithm.__name__(),
        'function': benchmark_function.__name__,
        'best': best,
        'results': results,
        'mean': mean,
        'stddev': stddev,
        'times': repeat_times
    }


def print_benchmark_results(benchmark_results):
    print("Algorithm:", benchmark_results['algorithm'])
    print("Function:", benchmark_results['function'])
    print("Best:", benchmark_results['best'])
    print("Mean:", benchmark_results['mean'])
    print("Standard deviation:", benchmark_results['stddev'])
    print("Results of", benchmark_results['times'], "repeats")
    for result in benchmark_results['results']:
        print(result)
