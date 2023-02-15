# First experiment, tests sums of minimum covers with static 8 nodes and increasing edges
from graph import create_random_graph, MVC, approx2
import matplotlib.pyplot as plot

mvc_sums = []
approx1_sums = []
approx2_sums = []
approx3_sums = []

for m in range(10):
    graphs = []
    for i in range(1000):
        g = create_random_graph(8, (m + 1) * 2)
        graphs.append(g)

    mvc_sum = 0
    a1_sum = 0
    a2_sum = 0
    a3_sum = 0
    for g in graphs:
        mvc_sum += len(MVC(g))
        # a1_sum += len(approx1(g))
        a2_sum += len(approx2(g))
        a3_sum += len(approx3(g))

    mvc_sums.append(mvc_sum)
    # approx1_sums.append(a1_sum)
    approx2_sums.append(a2_sum)
    approx3_sums.append(a3_sum)

plot.plot([2 * (x + 1) for x in range(10)], mvc_sums, label="Minimum Vertex Cover")
# plot.plot([2 * (x + 1) for x in range(10)], approx1_sums, label="Approximation 1")
plot.plot([2 * (x + 1) for x in range(10)], approx2_sums, label="Approximation 2")
plot.plot([2 * (x + 1) for x in range(10)], approx3_sums, label="Approximation 3")

plot.table("Approximations vs Actual MVC")
plot.xlabel("Graph Length")
plot.ylabel("Length of List of Vertex Cover")
plot.legend()
plot.savefig("graphs/experiment_3.png")
