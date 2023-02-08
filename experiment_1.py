import matplotlib.pyplot as plot
from experiment_2 import average_probabilities
from graph import Graph, has_cycle

NODE_CASES = [5, 10, 25, 50]
STEPS = 25
AVGS = 500

if __name__ == "__main__":
    proportions = list(range(0, 100, 100 // STEPS))

    for num_nodes in NODE_CASES:
        plot.plot(
            proportions,
            average_probabilities(num_nodes, proportions, AVGS, has_cycle),
            label=f"{num_nodes} nodes"
        )

    plot.title("Proportion of edges vs cycle probability")
    plot.ylabel("Cycle probability (%)")
    plot.xlabel("Proportion of edges (%)")
    plot.legend()
    plot.show()
