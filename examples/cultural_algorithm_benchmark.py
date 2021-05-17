from algorithms.physical.configurable.CulturalAlgorithm import CulturalAlgorithm
from benchmark.functions.ackley import ackley
from benchmark.functions.bukin_n6 import bukin_n6
from benchmark.functions.rastrigin import rastrigin
from benchmarking.benchmark_algorithm import benchmark, print_benchmark_results
from utilities.Bounds import Bounds

if __name__ == "__main__":
    ca = CulturalAlgorithm(100, 200, 20)
    for f, bounds in [(ackley, [Bounds(-32, 32), Bounds(-32, 32)]),
                      (bukin_n6, [Bounds(-15, -5), Bounds(-3, 3)]),
                      (rastrigin, [Bounds(-5.12, 5.12), Bounds(-5.12, 5.12)])]:
        print_benchmark_results(benchmark(ca, f, bounds))
        print()
