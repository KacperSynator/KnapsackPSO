import random
import math


class Particle:
    def __init__(self, dim):
        self.position = [random.choice([0, 1]) for _ in range(dim)]
        self.velocity = [random.uniform(-1, 1) for _ in range(dim)]
        self.pbest_position = self.position.copy()
        self.pbest_value = 0
    
    def update_velocity(self, pso_data, gbest_position):
        for i in range(len(self.velocity)):
            r1, r2 = random.uniform(0, 1), random.uniform(0, 1)
            cognitive_component = pso_data.cognitve * r1 * (self.pbest_position[i] - self.position[i])
            social_component = pso_data.social * r2 * (gbest_position[i] - self.position[i])
            self.velocity[i] = pso_data.inertia * self.velocity[i] + cognitive_component + social_component

    def update_position(self):
        for i in range(len(self.position)):
            # Apply sigmoid function to ensure binary values (0 or 1)
            self.position[i] = 1 if random.uniform(0, 1) < 1 / (1 + pow(math.e, -self.velocity[i])) else 0
