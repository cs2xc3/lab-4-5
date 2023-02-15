import matplotlib.pyplot as plot
from graph import Graph, max_unique_edges, create_random_graph, is_connected
from typing import Callable, List

NODE_CASES = [5, 10, 25, 50]
STEPS = 25
AVGS = 500

def average_probabilities(
    num_nodes: int,
    proportions: List[int],
    avgs: int,
    func: Callable[[Graph], bool]
) -> List[float]:
    max_edges = max_unique_edges(num_nodes)
    probabilities = []

    for proportion in proportions:
        edges = min(int(proportion / 100 * num_nodes), max_edges)
        outcomes = []

        for _ in range(avgs):
            G = create_random_graph(num_nodes, edges)
            if func(G):
                outcomes.append(100)
            else:
                outcomes.append(0)

        probabilities.append(outcomes)
        print(f"Completed {edges} edges with {num_nodes} nodes ({proportion}%)")

    return [sum(p) / avgs for p in probabilities]


if __name__ == "__main__":
    proportions = list(range(0, 500, 500 // STEPS))

    for num_nodes in NODE_CASES:
        plot.plot(
            proportions,
            average_probabilities(num_nodes, proportions, AVGS, is_connected),
            label=f"{num_nodes} nodes"
        )

    plot.title("Proportion of edges vs connected probability")
    plot.ylabel("Connected probability (%)")
    plot.xlabel("Proportion of edges to nodes (%)")
    plot.legend()
    plot.show()
