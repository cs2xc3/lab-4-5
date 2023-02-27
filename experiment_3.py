from graph import create_random_graph, MVC, approx1, approx2, approx3
import matplotlib.pyplot as plot

# First approximation experiment, tests sums of approximations with static 8 nodes and increasing edges
# First Test Case ~ 8 Nodes, 1 Edges
# Final Test Case ~ 8 Nodes, 28 Edges

approx1_sums = []
approx2_sums = []
approx3_sums = []
runs = 29

for m in range(1, runs):
    graphs = []
    for i in range(1000):
        g = create_random_graph(8, m)
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

plot.plot([x for x in range(1, runs)], approx1_sums, label="Approximation 1")
plot.plot([x for x in range(1, runs)], approx2_sums, label="Approximation 2")
plot.plot([x for x in range(1, runs)], approx3_sums, label="Approximation 3")

plot.title("Relative Length of Vertex Cover as Edges Increase")
plot.xlabel("Number of Edges")
plot.ylabel("Relative Length of Vertex Cover")
plot.legend()
plot.savefig("graphs/experiment_3_1.png")

# Second approximation experiment, tests sums of approximations with increasing num of nodes and 6 edges
# First Test Case ~ 4 Nodes, 6 Edges
# Final Test Case ~ 15 Nodes, 6 Edges

plot.clf()
approx1_sums.clear()
approx2_sums.clear()
approx3_sums.clear()
runs = 16

for m in range(4, runs):
    graphs = []
    for i in range(1000):
        g = create_random_graph(m, 6)
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

plot.plot([x for x in range(4, runs)], approx1_sums, label="Approximation 1")
plot.plot([x for x in range(4, runs)], approx2_sums, label="Approximation 2")
plot.plot([x for x in range(4, runs)], approx3_sums, label="Approximation 3")

plot.title("Relative Length of Vertex Cover as Nodes Increase")
plot.xlabel("Number of Nodes")
plot.ylabel("Relative Length of Vertex Cover")
plot.legend()
plot.savefig("graphs/experiment_3_2.png")

# Third approxximation experiment, tests sum of minimum covers with increasing num of nodes and proportional edges

plot.clf()
approx1_sums.clear()
approx2_sums.clear()
approx3_sums.clear()
runs = 8

for m in range(runs):
    graphs = []
    for i in range(1000):
        g = create_random_graph(m + 4, (m + 4) / 2)
        graphs.append(g)
    
    mvc_sum = 0
    a1_sum  = 0
    a2_sum  = 0
    a3_sum  = 0

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

plot.title("Relative Length of Vertex Cover as Graph Increases")
plot.xlabel("Number of Nodes (with proportional edges)")
plot.ylabel("Relative Length of Vertex Cover")
plot.legend()
plot.savefig("graphs/experiment_3_3.png")
