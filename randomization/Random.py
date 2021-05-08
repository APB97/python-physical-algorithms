from random import random, randint
from typing import List

from utilities.Bounds import Bounds


class Random:

    @staticmethod
    def from_range(start, end, digits: int = None):
        r = random() * (end - start) + start
        if digits is not None:
            return round(r, digits)
        return r

    @staticmethod
    def vector_in_bounds(bounds: List[Bounds], digits: int = None):
        vector = [Random.from_range(b.minimum, b.maximum) for b in bounds]
        if digits is not None:
            return [round(v, digits) for v in vector]
        return vector

    @staticmethod
    def bits(count: int):
        return [randint(0, 1) for _ in range(count)]
