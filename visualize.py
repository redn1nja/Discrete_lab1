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

from time import perf_counter


def visualize_mstp(G):
    plt.figure(1)
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True)
    weights = dict([(data[0:2], data[2]["weight"]) for data in G.edges(data=True)])
    print(f"Graph total weight: {sum(list(weights.values()))}")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=weights)

    plt.figure(2)
    P = generate_mst_prim(G)
    pos = nx.spring_layout(P)
    nx.draw(P, pos, with_labels=True)
    weights = dict([(data[0:2], data[2]["weight"]) for data in P.edges(data=True)])
    print(f"Graph total weight: {sum(list(weights.values()))}")
    nx.draw_networkx_edge_labels(P, pos, edge_labels=weights)

    plt.figure(3)
    K = generate_mst_kruskal(G)
    pos = nx.spring_layout(K)
    nx.draw(K, pos, with_labels=True)
    weights = dict([(data[0:2], data[2]["weight"]) for data in K.edges(data=True)])
    print(f"Graph total weight: {sum(list(weights.values()))}")
    nx.draw_networkx_edge_labels(K, pos, edge_labels=weights)

    plt.figure(4)
    M = minimum_spanning_tree(G)
    pos = nx.spring_layout(M)
    nx.draw(M, pos, with_labels=True)
    weights = dict([(data[0:2], data[2]["weight"]) for data in M.edges(data=True)])
    print(f"Graph total weight: {sum(list(weights.values()))}")
    nx.draw_networkx_edge_labels(M, pos, edge_labels=weights)

    plt.show()


if __name__ == "__main__":
    G = gnp_random_connected_graph(8, 0.4)
    t = perf_counter()
    T = generate_mst_kruskal(G)
    t = perf_counter() - t
    print(t)
    visualize_mstp(G)
