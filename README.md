# Physical algorithms in Python

> Physical algorithms from Jason Brownlee's book "Clever Algorithms: Nature-Inspired Programming Recipes"
> implemented in Python

## Table of contents

1. [Description](#description)
2. [How to use](#how-to-use)
3. [License](#license)

## Description

This is the project for "Selected Artificial Intelligence Methods", 
and it was finished around April 30th of 2021.

At first, it seemed like understanding the Ruby programming language would be the hardest task for me.
I had thought this way because inside the book not everything was clear about the language
until I checked the online documentation to resolve my doubts.

Later, during implementation of Extremal Optimization (EO) I was stuck
when trying to use it for continuous function optimization.
I ended up looking for resources about the EO, and after many searches,
I found one article that was matching my needs, written by Fleford Redoloza and Liangping Li.
It was really helpful, and I finished implementing the EO.
One thing "missing" from the implementation (compared to original) was the tau parameter.

Implemented algorithms:
- Simulated Annealing
- Extremal Optimization
- Harmony Search
- Cultural Algorithm
- Memetic Algorithm

Implemented benchmark functions:
- Ackley
- Bukin no. 6
- Rastrigin

Technologies used:
- Python 3
    - list comprehensions
    - a random module for random and randint functions
    - math module for exp, inf, sqrt functions
    - numpy library (only for numpy.random.mtrand.randn function)

[Back to the top](#physical-algorithms-in-python)

## How to use

Instruction for "Universal" variants:

1. Pick a benchmark (or other function to optimize)
2. Choose problem bounds
3. Pick an algorithm to use
4. Use the following code for reference

```python
from benchmark.functions.ackley import ackley  # benchmark function import
from algorithms.physical.universal.cultural_algorithm_any_func import search  # algorithm import

if __name__ == "__main__":
  problem_bounds = [[-32, 32], [-32, 32]]  # problem domain
  result = search(ackley, 50, problem_bounds, 100, 20, print_progress=False)
  print(result)

```

[Back to the top](#physical-algorithms-in-python)

## License

See this project's license (MIT License) [here](LICENSE)

[Back to the top](#physical-algorithms-in-python)
