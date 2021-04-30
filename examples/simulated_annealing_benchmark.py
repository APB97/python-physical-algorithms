from benchmark.functions.ackley import ackley
from benchmark.functions.bukin_n6 import bukin_n6
from benchmark.functions.rastrigin import rastrigin
from benchmarking.ConfiguredSearch import ConfiguredSearch
from algorithms.physical.configurable.SimulatedAnnealing import SimulatedAnnealing
from benchmarking.benchmark import benchmark, print_benchmark_results

if __name__ == "__main__":
    sa = SimulatedAnnealing(2000, 100000, 0.98)
    for f, bounds in [(ackley, [[-32, 32], [-32, 32]]),
                      (bukin_n6, [[-15, -5], [-3, 3]]),
                      (rastrigin, [[-5.12, 5.12], [-5.12, 5.12]])]:
        print_benchmark_results(benchmark(ConfiguredSearch(sa, f, bounds)))
        print()
