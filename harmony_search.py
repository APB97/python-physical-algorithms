from random import random, randint


def objective_function(vector):
    value = sum([x ** 2 for x in vector])
    return value


def rand_in_bounds(min_range, max_range):
    return min_range + random() * (max_range - min_range)


def random_vector(search_space):
    return [rand_in_bounds(space[0], space[1]) for space in search_space]


def create_random_harmony(search_space):
    harmony = {'vector': random_vector(search_space)}
    harmony['fitness'] = objective_function(harmony['vector'])
    return harmony


def init_harmony_memory(search_space, mem_size, factor=3):
    memory = [create_random_harmony(search_space) for _ in range(0, mem_size*factor)]

    def sorting_key(mem_cell):
        return mem_cell['fitness']

    memory.sort(key=sorting_key)
    return memory[0:mem_size]


def create_harmony(search_space, memory, consider_rate, adjust_rate, harm_range):
    vector = [i for i in range(0, len(search_space))]
    for i in vector:
        if random() < consider_rate:
            value = memory[randint(0, len(memory) - 1)]['vector'][i]
            if random() < adjust_rate:
                value += harm_range * rand_in_bounds(-1.0, 1.0)
                if value < search_space[i][0]:
                    value = search_space[i][0]
                if value > search_space[i][1]:
                    value = search_space[i][1]
                    vector[i] = value
        else:
            vector[i] = rand_in_bounds(search_space[i][0], search_space[i][1])
    return {'vector': vector}


def search(bounds, max_iter, mem_size, consider_rate, adjust_rate, harmony_range, print_progress=False):
    mem = init_harmony_memory(bounds, mem_size)
    best = mem[0]

    def sorting_key(harmony):
        return harmony['fitness']

    for i in range(max_iter):
        harm = create_harmony(bounds, mem, consider_rate, adjust_rate, harmony_range)
        harm['fitness'] = objective_function(harm['vector'])
        if harm['fitness'] < best['fitness']:
            best = harm
        mem.append(harm)
        mem.sort(key=sorting_key)
        mem.remove(mem[len(mem) - 1])  # remove worst value
        if print_progress:
            print(f"iteration={i}, fitness={best['fitness']}")

    return best


if __name__ == "__main__":
    problem_size = 3
    problem_bounds = [[-5, 5] for _ in range(problem_size)]
    # algorithm configuration
    memory = 20
    consider = 0.95
    adjust = 0.7
    harm_range = 0.05
    iters = 500
    # execution
    best_found = search(problem_bounds, iters, memory, consider, adjust, harm_range, print_progress=True)
    print(f"Done. Solution f={best_found['fitness']}, input={best_found['vector']}")
