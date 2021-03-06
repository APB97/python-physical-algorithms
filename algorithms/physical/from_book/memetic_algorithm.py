from random import random, randint


def objective_function(vector):
    value = sum([x ** 2 for x in vector])
    return value


def random_bitstring(num_bits):
    return [randint(0, 1) for _ in range(num_bits)]


def decode(bitstring, search_space, bits_per_param):
    vector = [0 for _ in range(len(search_space))]
    for i in range(len(search_space)):
        offset, total_sum = i * bits_per_param, 0.0
        param = list(reversed(bitstring[offset:offset + bits_per_param]))
        total_sum = sum([param[j] * 2 ** j for j in range(len(param))])
        min_bound, max_bound = search_space[i]
        vector[i] = min_bound + ((max_bound - min_bound) / ((2 ** bits_per_param) - 1.0)) * total_sum
    return vector


def fitness(candidate, search_space, param_bits):
    candidate['vector'] = decode(candidate['bitstring'], search_space, param_bits)
    candidate['fitness'] = objective_function(candidate['vector'])


def binary_tournament(pop):
    i, j = randint(0, len(pop) - 1), randint(0, len(pop) - 1)
    while j == i:
        j = randint(0, len(pop) - 1)
    if pop[i]['fitness'] < pop[j]['fitness']:
        return pop[i]
    else:
        return pop[j]


def negate(bit):
    if bit == 1:
        return 0
    else:
        return 1


def point_mutation(bitstring, rate=None):
    if rate is None:
        rate = 1.0 / len(bitstring)

    def consider_negate(bit):
        if random() < rate:
            return negate(bit)
        else:
            return bit

    return [consider_negate(bit) for bit in bitstring]


def crossover(parent1, parent2, rate):
    if random() >= rate:
        return list(parent1)

    def random_pick(index):
        if random() < 0.5:
            return parent1[index]
        else:
            return parent2[index]

    return [random_pick(i) for i in range(len(parent1))]


def reproduce(selected, pop_size, p_cross, p_mut):
    children = []
    steps = [1, -1]
    for i in range(len(selected)):
        p2 = selected[i + steps[i % 2]]
        if i == len(selected) - 1:
            p2 = selected[0]
        bitstring = crossover(selected[i]['bitstring'], p2['bitstring'], p_cross)
        bitstring = point_mutation(bitstring, p_mut)
        children.append({'bitstring': bitstring})
        if len(children) >= pop_size:
            break
    return children


def bitclimber(child, search_space, p_mut, max_local_gens, bits_per_param):
    current = child
    for i in range(max_local_gens):
        candidate = {'bitstring': point_mutation(current['bitstring'], p_mut)}
        fitness(candidate, search_space, bits_per_param)
        if candidate['fitness'] <= current['fitness']:
            current = candidate
    return current


def search(max_gens, search_space, pop_size, p_cross, p_mut, max_local_gens, p_local, bits_per_param=16):
    pop = [{'bitstring': random_bitstring(len(search_space) * bits_per_param)} for _ in range(pop_size)]
    for candidate in pop:
        fitness(candidate, search_space, bits_per_param)

    def key(cand):
        return cand['fitness']

    pop.sort(key=key)
    gen, best = 0, pop[0]
    for i in range(1, max_gens):
        selected = [binary_tournament(pop) for _ in range(pop_size)]
        children = reproduce(selected, pop_size, p_cross, p_mut)
        for c in children:
            fitness(c, search_space, bits_per_param)
        pop = []
        for c in children:
            if random() < p_local:
                c = bitclimber(c, search_space, p_mut, max_local_gens, bits_per_param)
            pop.append(c)
        pop.sort(key=key)
        if pop[0]['fitness'] <= best['fitness']:
            best = pop[0]
        print(f"gen={i}, f={best['fitness']}, b={best['bitstring']}")
    return best


if __name__ == "__main__":
    problem_size = 3
    problem_bounds = [[-5, 5] for _ in range(problem_size)]
    # algorithm configuration
    generations = 100
    population_size = 100
    prob_cross = 0.98
    prob_mut = 1.0/(problem_size * 16)
    max_local_generations = 20
    prob_local = 0.5
    # execution
    best_found = search(generations, problem_bounds, population_size,
                        prob_cross, prob_mut, max_local_generations, prob_local)
    bits = ''.join([str(b) for b in best_found['bitstring']])
    print(f"Done. Solution f={best_found['fitness']}, b={bits}, input={best_found['vector']}")
