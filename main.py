import matplotlib.pyplot as plt
import numpy as np

from pso import PSOData, pso_knapsack

WEIGHTS = [
    382745, 799601, 909247, 729069, 467902, 44328, 34610, 698150, 823460, 903959, 853665, 551830,
    610856, 670702, 488960, 951111, 323046, 446298, 931161, 31385, 496951, 264724, 224916, 169684,
]

PRICES = [
    825594, 1677009, 1676628, 1523970, 943972, 97426, 69666, 1296457, 1679693, 1902996, 1844992,
    1049289, 1252836, 1319836, 953277, 2067538, 675367, 853655, 1826027, 65731, 901489, 577243,
    466257, 369261,
]

CAPACITY = 6404180
OPTIMAL = 13549094

PARTICLES = 500
ITERATIONS = 100
COGNITIVE = 2.0
SOCIAL = 2.0
INERTIA = 0.9

N_REPS = 10

def plot_and_save(iteration_values, title, filename):
    plt.plot(range(1, ITERATIONS + 1), iteration_values, label='Best Value')
    plt.axhline(y=OPTIMAL, color='r', linestyle='--', label='Optimal Value')
    plt.xlabel('Iteration')
    plt.ylabel('Best Value')
    plt.title(title)
    plt.legend()

    plt.savefig(filename)
    plt.close

if __name__ == "__main__":
    data = PSOData(
        weights=WEIGHTS,
        prices=PRICES,
        capacity=CAPACITY,
        num_particles=PARTICLES,
        max_iterations=ITERATIONS,
        cognitve=COGNITIVE,
        social=SOCIAL,
        inertia=INERTIA
    )

    best_position = None
    best_value = None
    result = None

    for cognitve in np.arange(0.1, 4.0, 0.5):
        for social in np.arange(0.1, 4.0, 0.5):
            n_optimal = 0
            data.cognitve = cognitve
            data.social = social
            for _ in range(N_REPS):
                result = pso_knapsack(data)

                if result.best_value == OPTIMAL:
                    n_optimal += 1

            plot_and_save(result.iteration_values,
                            title=f"cog={cognitve} so={social} in={INERTIA}",
                            filename=f"graphs/cog{cognitve}so{social}in{INERTIA}.png")
                
            print(f"cog={cognitve} so={social} in={INERTIA}")
            print(f"Accuracy: {n_optimal / N_REPS}", )
            print(f"Items included: {result.best_position}")
            print(f"Total Value: {result.best_value}")
            print("")

    
