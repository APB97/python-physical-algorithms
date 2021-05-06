from benchmarking.ConfigurableAlgorithmBase import ConfigurableAlgorithmBase
from randomization.Random import Random


class ExtremalOptimization(ConfigurableAlgorithmBase):
    def __init__(self, max_iterations, eps):
        super().__init__(self.__call__)
        self.eps = eps
        self.max_iterations = max_iterations

    @property
    def __name__(self):
        return "Extremal Optimization"

    def __call__(self, function, bounds):
        return self.__extremal_optimization(function, bounds)

    def __extremal_optimization(self, function, bounds):
        current = {'input': Random.vector_in_bounds(bounds)}
        current['value'] = function(current['input'])
        best = current

        for i in range(self.max_iterations):
            candidate = {'input': list.copy(current['input'])}
            fits = [function([candidate['input'][i]]) for i in range(len(bounds))]
            best_component = fits.index(min(fits))
            worst_component = fits.index(max(fits))
            dist_max = max([abs(x - y) for x in candidate['input'] for y in candidate['input']])
            u = Random.from_range(-1, 1, 2)
            if dist_max < self.eps:
                dist_max = bounds[0].maximum
            new_component = candidate['input'][best_component] + dist_max * u
            candidate['input'][worst_component] = new_component
            candidate['value'] = function(candidate['input'])
            current = candidate
            if candidate['value'] < best['value']:
                best = candidate
        return best
