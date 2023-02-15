# First approximation experiment, tests sums of minimum covers with static 8 nodes and increasing edges
from graph import create_random_graph, MVC, approx1, approx2, approx3
import matplotlib.pyplot as plot

approx1_sums = []
approx2_sums = []
approx3_sums = []
runs = 15

for m in range(1, runs):
    graphs = []
    for i in range(1000):
        g = create_random_graph(8, m * 2)
        graphs.append(g)

    mvc_sum = 0
    a1_sum = 0
    a2_sum = 0
    a3_sum = 0
    for g in graphs:
        mvc_sum += len(MVC(g))
        a1_sum += len(approx1(g))
        a2_sum += len(approx2(g))
        a3_sum += len(approx3(g))

    approx1_sums.append(a1_sum / mvc_sum)
    approx2_sums.append(a2_sum / mvc_sum)
    approx3_sums.append(a3_sum / mvc_sum)

plot.plot([2 * x for x in range(1, runs)], approx1_sums, label="Approximation 1")
plot.plot([2 * x for x in range(1, runs)], approx2_sums, label="Approximation 2")
plot.plot([2 * x for x in range(1, runs)], approx3_sums, label="Approximation 3")

plot.title("Approximations vs Actual MVC (1)")
plot.xlabel("Number of Edges")
plot.ylabel("Expected Performance")
plot.legend()
plot.savefig("graphs/experiment_3_1.png")

# Second approximation experiment, tests sums of minimum covers with increasing num of nodes and 6 edges

plot.clf()
approx1_sums.clear()
approx2_sums.clear()
approx3_sums.clear()
runs = 8

for m in range(runs):
    graphs = []
    for i in range(1000):
        g = create_random_graph(m + 4, 6)
        graphs.append(g)

    mvc_sum = 0
    a1_sum = 0
    a2_sum = 0
    a3_sum = 0
    for g in graphs:
        mvc_sum += len(MVC(g))
        a1_sum += len(approx1(g))
        a2_sum += len(approx2(g))
        a3_sum += len(approx3(g))

    approx1_sums.append(a1_sum / mvc_sum)
    approx2_sums.append(a2_sum / mvc_sum)
    approx3_sums.append(a3_sum / mvc_sum)

plot.plot([x + 4 for x in range(runs)], approx1_sums, label="Approximation 1")
plot.plot([x + 4 for x in range(runs)], approx2_sums, label="Approximation 2")
plot.plot([x + 4 for x in range(runs)], approx3_sums, label="Approximation 3")

plot.title("Approximations vs Actual MVC (2)")
plot.xlabel("Number of Nodes")
plot.ylabel("Expected Performance")
plot.legend()
plot.savefig("graphs/experiment_3_2.png")
