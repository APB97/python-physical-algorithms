from random import random
from typing import List

from utilities.Bounds import Bounds


class Random:

    @staticmethod
    def from_range(start, end, digits):
        return round(Random.from_range(start, end), digits)

    @staticmethod
    def from_range(start, end):
        return random() * (end - start) + start

    @staticmethod
    def vector_in_bounds(bounds: List[Bounds]):
        return [Random.from_range(b.minimum, b.maximum) for b in bounds]

    @staticmethod
    def vector_in_bounds(bounds: List[Bounds], digits: int):
        return [round(v, digits) for v in Random.vector_in_bounds(bounds)]
