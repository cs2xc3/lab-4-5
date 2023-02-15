import matplotlib.pyplot as plot
from experiment_2 import average_probabilities
from graph import Graph, has_cycle, create_random_graph

NODE_CASES = [5, 10, 25, 50]
STEPS = 25
AVGS = 500

def cycle_probability(num_nodes, proportions, avgs):
    maximum_edges = num_nodes
    probabilities = []

    for proportion in proportions:
        edges = int(proportion / 100 * maximum_edges)
        outcomes = []

        for _ in range(avgs):
            G = create_random_graph(num_nodes, edges)
            if has_cycle(G):
                outcomes.append(100)
            else:
                outcomes.append(0)

        probabilities.append(outcomes)
        print(f"Completed {edges} edges with {num_nodes} nodes ({proportion}%)")

    return [sum(p) / avgs for p in probabilities]


if __name__ == "__main__":
    proportions = list(range(0, 100, 100 // STEPS))

    for num_nodes in NODE_CASES:
        plot.plot(
            proportions,
            cycle_probability(num_nodes, proportions, AVGS),
            label=f"{num_nodes} nodes"
        )

    plot.title("Proportion of edges vs cycle probability")
    plot.ylabel("Cycle probability (%)")
    plot.xlabel("Proportion of edges (%)")
    plot.legend()
    plot.show()
