from particle import Particle

class PSOData(object):
    def __init__(self, weights, prices, capacity, num_particles, max_iterations, cognitve, social, inertia):
        self.weights = weights
        self.prices = prices
        self.capacity = capacity
        self.num_particles = num_particles
        self.max_iterations = max_iterations
        self.cognitve = cognitve
        self.social = social
        self.inertia = inertia

class PSOResult(object):
    def __init__(self, best_value, best_position, iteration_values):
        self.best_value = best_value
        self.best_position = best_position
        self.iteration_values = iteration_values


def knapsack_fitness(pso_data, solution):
    total_weight = sum(solution[i] * pso_data.weights[i] for i in range(len(solution)))
    total_value = sum(solution[i] * pso_data.prices[i] for i in range(len(solution)))

    if total_weight > pso_data.capacity:
        return 0  # Penalize solutions that exceed the knapsack capacity
    else:
        return total_value

def pso_knapsack(pso_data):
    particles = [Particle(len(pso_data.weights)) for _ in range(pso_data.num_particles)]
    gbest = max(particles, key=lambda x: knapsack_fitness(pso_data, x.position))
    gbest_position = gbest.position.copy()

    best_values = []

    for _ in range(pso_data.max_iterations):
        for particle in particles:
            fitness = knapsack_fitness(pso_data, particle.position)
            if fitness > knapsack_fitness(pso_data, particle.pbest_position):
                particle.pbest_position = particle.position.copy()
                particle.pbest_value = fitness

            if fitness > knapsack_fitness(pso_data, gbest_position):
                gbest_position = particle.position.copy()

        for particle in particles:
            particle.update_velocity(pso_data, gbest_position)
            particle.update_position()
        
        best_values.append(knapsack_fitness(pso_data, gbest_position))

    return PSOResult(
        best_value=knapsack_fitness(pso_data, gbest_position),
        best_position=[i + 1 for i in range(len(gbest_position)) if gbest_position[i] == 1],
        iteration_values=best_values
    )
