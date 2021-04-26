from math import inf
from random import random, randint


def objective_function(vector):
    value = sum([x ** 2 for x in vector])
    return value


def rand_in_bounds(min_range, max_range):
    return min_range + random() * (max_range - min_range)


def random_vector(search_space):
    return [rand_in_bounds(space[0], space[1]) for space in search_space]


def mutate_with_inf(candidate, beliefs, search_space):
    vector = [0 for _ in range(len(candidate['vector']))]
    for i in range(len(candidate['vector'])):
        vector[i] = rand_in_bounds(beliefs['normative'][i][0], beliefs['normative'][i][1])
        if vector[i] < search_space[i][0]:
            vector[i] = search_space[i][0]
        if vector[i] > search_space[i][1]:
            vector[i] = search_space[i][1]
    return {'vector': vector}


def binary_tournament(pop):
    i, j = randint(0, len(pop) - 1), randint(0, len(pop) - 1)
    while j == i:
        j = randint(0, len(pop) - 1)
    if pop[i]['fitness'] < pop[j]['fitness']:
        return pop[i]
    else:
        return pop[j]


def initialize_beliefspace(search_space):
    belief_space = {'situational': None, 'normative': [list.copy(space) for space in search_space]}
    return belief_space


def update_beliefspace_situational(belief_space, best):
    current_best = belief_space['situational']
    if current_best is None or best['fitness'] < current_best['fitness']:
        belief_space['situational'] = best


def min_component(accepted, i):
    min_comp = inf
    for single in accepted:
        if single['vector'][i] < min_comp:
            min_comp = single['vector'][i]
    return min_comp


def update_beliefspace_normative(beliefspace, accepted):
    for i in range(len(beliefspace['normative'])):
        beliefspace['normative'][i][0] = min([a['vector'][i] for a in accepted])
        beliefspace['normative'][i][1] = max([a['vector'][i] for a in accepted])


def search(max_gens, search_space, pop_size, num_accepted):
    pop = [{'vector': random_vector(search_space)} for _ in range(pop_size)]
    belief_space = initialize_beliefspace(search_space)
    for p in pop:
        p['fitness'] = objective_function(p['vector'])

    def key(member):
        return member['fitness']

    pop.sort(key=key)
    best = pop[0]
    update_beliefspace_situational(belief_space, best)
    for i in range(1, max_gens + 1):
        children = [mutate_with_inf(pop[j], belief_space, search_space) for j in range(pop_size)]
        for c in children:
            c['fitness'] = objective_function(c['vector'])
        children.sort(key=key)
        best = children[0]
        update_beliefspace_situational(belief_space, best)
        pop = [binary_tournament(pop + children) for _ in range(pop_size)]
        pop.sort(key=key)
        accepted = pop[0:num_accepted]
        update_beliefspace_normative(belief_space, accepted)
        print(f"generation={i}, f={belief_space['situational']['fitness']}")

    return belief_space['situational']


if __name__ == "__main__":
    problem_size = 2
    problem_bounds = [[-5, 5] for _ in range(problem_size)]
    # algorithm configuration
    generations = 200
    population_size = 100
    number_accepted = population_size // 5
    # execution
    best_found = search(generations, problem_bounds, population_size, number_accepted)
    print(f"Done. Solution f={best_found['fitness']}, input={best_found['vector']}")
