"""
Module visualizing Prim's and Kruskal's minimum
spanning tree generation algorithms
"""
from prim import generate_mst_prim
from kruskal import generate_mst_kruskal
from graph_gen import gnp_random_connected_graph

import networkx as nx
from networkx.algorithms import minimum_spanning_tree
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

from time import perf_counter


def visualize_mstp(G: nx.Graph) -> None:
    """
    Visualizes trees created by mst algorithms.
    """
    plt.figure(1)
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True)
    weights = dict([(data[0:2], data[2]["weight"]) for data in G.edges(data=True)])
    print(f"Graph total weight: {sum(list(weights.values()))}")
    print("Graph edges:", list(G.edges(data=True)))
    print("Total:", len(G.edges()))
    nx.draw_networkx_edge_labels(G, pos, edge_labels=weights)

    plt.figure(2)
    P = generate_mst_prim(G)
    pos = nx.spring_layout(P)
    nx.draw(P, pos, with_labels=True)
    weights = dict([(data[0:2], data[2]["weight"]) for data in P.edges(data=True)])
    print(f"Prim total weight: {sum(list(weights.values()))}")
    nx.draw_networkx_edge_labels(P, pos, edge_labels=weights)

    plt.figure(3)
    K = generate_mst_kruskal(G)
    pos = nx.spring_layout(K)
    nx.draw(K, pos, with_labels=True)
    weights = dict([(data[0:2], data[2]["weight"]) for data in K.edges(data=True)])
    print(f"Kruskal total weight: {sum(list(weights.values()))}")
    nx.draw_networkx_edge_labels(K, pos, edge_labels=weights)

    plt.figure(4)
    M = minimum_spanning_tree(G)
    pos = nx.spring_layout(M)
    nx.draw(M, pos, with_labels=True)
    weights = dict([(data[0:2], data[2]["weight"]) for data in M.edges(data=True)])
    print(f"Builtin algorithm total weight: {sum(list(weights.values()))}")
    nx.draw_networkx_edge_labels(M, pos, edge_labels=weights)

    plt.show()


def plot_algorithm_comparisons() -> None:
    """
    Plots comparisons of runtimes of three available algorithms.
    """
    graph_sizes = tuple(range(10, 200, 5))
    print(graph_sizes)
    prim_times = []
    kruskal_times = []
    builtin_times = []
    for node_num in graph_sizes:
        G = gnp_random_connected_graph(node_num, 1)
        t = perf_counter()
        generate_mst_prim(G)
        prim_times.append(perf_counter() - t)

        t = perf_counter()
        generate_mst_kruskal(G)
        kruskal_times.append(perf_counter() - t)

        t = perf_counter()
        minimum_spanning_tree(G)
        builtin_times.append(perf_counter() - t)

    fig, ax = plt.subplots()
    plt.plot(graph_sizes, prim_times, "b-")
    prim_patch = mpatches.Patch(color="blue", label="Prim")
    plt.plot(graph_sizes, kruskal_times, "r-")
    kruskal_patch = mpatches.Patch(color='red', label='Kruskal')
    plt.plot(graph_sizes, builtin_times, "g-")
    builtin_patch = mpatches.Patch(color="green", label="Builtin")

    ax.legend(handles=[kruskal_patch, prim_patch, builtin_patch])
    plt.xlabel("Number of graph nodes")
    plt.ylabel("Execution time, secs")

    plt.show()


if __name__ == "__main__":
    G = gnp_random_connected_graph(8, 0.4)
    # t = perf_counter()
    # T = generate_mst_kruskal(G)
    # t = perf_counter() - t
    # print(t)
    # visualize_mstp(G)
    plot_algorithm_comparisons()

