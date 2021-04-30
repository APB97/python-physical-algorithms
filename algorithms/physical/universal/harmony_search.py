from random import random, randint


def rand_in_bounds(min_range, max_range):
    return min_range + random() * (max_range - min_range)


def random_vector(search_space):
    return [rand_in_bounds(space[0], space[1]) for space in search_space]


def create_random_harmony(objective_function, search_space):
    harmony = {'input': random_vector(search_space)}
    harmony['value'] = objective_function(harmony['input'])
    return harmony


def init_harmony_memory(objective_function, search_space, mem_size, factor=3):
    memory = [create_random_harmony(objective_function, search_space) for _ in range(0, mem_size*factor)]

    def sorting_key(mem_cell):
        return mem_cell['value']

    memory.sort(key=sorting_key)
    return memory[0:mem_size]


def create_harmony(search_space, memory, consider_rate, adjust_rate, harm_range):
    vector = [i for i in range(0, len(search_space))]
    for i in vector:
        if random() < consider_rate:
            value = memory[randint(0, len(memory) - 1)]['input'][i]
            if random() < adjust_rate:
                value += harm_range * rand_in_bounds(-1.0, 1.0)
                if value < search_space[i][0]:
                    value = search_space[i][0]
                if value > search_space[i][1]:
                    value = search_space[i][1]
            vector[i] = value
        else:
            vector[i] = rand_in_bounds(search_space[i][0], search_space[i][1])
    return {'input': vector}


def search(objective_function, bounds, max_iter, mem_size,
           consider_rate, adjust_rate, harm_range, print_progress=False):
    memory = init_harmony_memory(objective_function, bounds, mem_size)
    best = memory[0]

    def sorting_key(harmony):
        return harmony['value']

    for i in range(max_iter):
        harm = create_harmony(bounds, memory, consider_rate, adjust_rate, harm_range)
        harm['value'] = objective_function(harm['input'])
        if harm['value'] < best['value']:
            best = harm
        memory.append(harm)
        memory.sort(key=sorting_key)
        memory.remove(memory[len(memory) - 1])  # remove worst value
        if print_progress:
            print(f"iteration={i}, fitness={best['value']}")

    return best
