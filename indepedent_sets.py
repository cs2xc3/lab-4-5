import matplotlib.pyplot as plot
from graph import MVC, MIS, max_unique_edges, create_random_graph

# MIS function can be found in graph.py

NODES = 10
CASES = 250

if __name__ == "__main__":
    max_edges = max_unique_edges(NODES)
    edge_cases = range(max_edges + 1)
    average_mvc_lens = []
    average_mis_lens = []

    for edges in edge_cases:
        print(f"Trying {edges} / {max_edges} edges")
        mvc_sum = 0
        mis_sum = 0

        for c in range(CASES):
            G = create_random_graph(NODES, edges)
            mvc_sum += len(MVC(G))
            mis_sum += len(MIS(G))

        average_mvc_lens.append(mvc_sum / CASES)
        average_mis_lens.append(mis_sum / CASES)

    sums = [average_mvc_lens[i] + average_mis_lens[i] for i in range(len(edge_cases))]

    plot.plot(edge_cases, average_mvc_lens, label=f"MVC")
    plot.plot(edge_cases, average_mis_lens, label=f"MIS")
    plot.plot(edge_cases, sums, label="Sum")

    plot.title(f"Relation between MVC and MIS (n={NODES})")
    plot.ylabel("Average Size")
    plot.xlabel("Number of Edges")
    plot.legend()
    plot.show()
