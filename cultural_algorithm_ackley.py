from random import random, randint

from ackley import ackley


def objective_function(vector):
    value = ackley(vector)
    return value


def rand_in_bounds(min_range, max_range):
    return min_range + random() * (max_range - min_range)


def random_vector(search_space):
    return [rand_in_bounds(space[0], space[1]) for space in search_space]


def mutate_with_inf(candidate, beliefs, search_space):
    vector = [0 for _ in range(len(candidate['input']))]
    for i in range(len(candidate['input'])):
        vector[i] = rand_in_bounds(beliefs['normative'][i][0], beliefs['normative'][i][1])
        if vector[i] < search_space[i][0]:
            vector[i] = search_space[i][0]
        if vector[i] > search_space[i][1]:
            vector[i] = search_space[i][1]
    return {'input': vector}


def binary_tournament(pop):
    i, j = randint(0, len(pop) - 1), randint(0, len(pop) - 1)
    while j == i:
        j = randint(0, len(pop) - 1)
    if pop[i]['value'] < pop[j]['value']:
        return pop[i]
    else:
        return pop[j]


def initialize_beliefspace(search_space):
    belief_space = {'situational': None, 'normative': [list.copy(space) for space in search_space]}
    return belief_space


def update_beliefspace_situational(belief_space, best):
    current_best = belief_space['situational']
    if current_best is None or best['value'] < current_best['value']:
        belief_space['situational'] = best


def update_beliefspace_normative(beliefspace, accepted):
    for i in range(len(beliefspace['normative'])):
        beliefspace['normative'][i][0] = min([a['input'][i] for a in accepted])
        beliefspace['normative'][i][1] = max([a['input'][i] for a in accepted])


def search_ackley(max_gens, search_space, pop_size, num_accepted, print_progress=False):
    pop = [{'input': random_vector(search_space)} for _ in range(pop_size)]
    belief_space = initialize_beliefspace(search_space)
    for p in pop:
        p['value'] = objective_function(p['input'])

    def key(member):
        return member['value']

    pop.sort(key=key)
    best = pop[0]
    update_beliefspace_situational(belief_space, best)
    for i in range(1, max_gens + 1):
        children = [mutate_with_inf(pop[j], belief_space, search_space) for j in range(pop_size)]
        for c in children:
            c['value'] = objective_function(c['input'])
        children.sort(key=key)
        best = children[0]
        update_beliefspace_situational(belief_space, best)
        pop = [binary_tournament(pop + children) for _ in range(pop_size)]
        pop.sort(key=key)
        accepted = pop[0:num_accepted]
        update_beliefspace_normative(belief_space, accepted)
        if print_progress:
            print(f"generation={i}, f={belief_space['situational']['value']}")

    return belief_space['situational']


if __name__ == "__main__":
    problem_size = 2
    problem_bounds = [[-32, 32] for _ in range(problem_size)]
    # algorithm configuration
    generations = 200
    population_size = 100
    number_accepted = population_size // 5
    # execution
    best_found = search_ackley(generations, problem_bounds, population_size, number_accepted, print_progress=True)
    print(f"Done. Solution f={best_found['value']}, input={best_found['input']}")
