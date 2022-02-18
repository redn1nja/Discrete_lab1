import random
import networkx as nx
from itertools import combinations, groupby
from tqdm import tqdm
import time


def gnp_random_connected_graph(num_of_nodes: int,
                               completeness: int) -> list:
    """
    Generates a random undirected graph, similarly to an Erdős-Rényi 
    graph, but enforcing that the resulting graph is conneted
    """
    weight = []
    edges = combinations(range(num_of_nodes), 2)
    G = nx.Graph()
    G.add_nodes_from(range(num_of_nodes))

    for _, node_edges in groupby(edges, key=lambda x: x[0]):
        node_edges = list(node_edges)
        random_edge = random.choice(node_edges)
        G.add_edge(*random_edge)
        for e in node_edges:
            if random.random() < completeness:
                G.add_edge(*e)

    for (u, v, w) in G.edges(data=True):
        w['weight'] = random.randint(0, 10)
        weight.append(w['weight'])

    return G, weight


def crascal(graph):
    # edges = graph[0]
    vertexes = graph[0]
    weights = graph[1]
    edges = list(vertexes.edges())
    edges = list(zip(edges, weights))
    # print(edges)
    # set_of_vertex = set()
    # for item in edges:
    #     for number in item[0]:
    #         set_of_vertex.add(number)
    # list_of_sets = []
    # for item in set_of_vertex:
    #     list_of_sets.append({item})
    list_of_sets=[{i} for i in list(vertexes.nodes())]
    ver = sorted(edges, key=lambda x: x[1])
    # print(edges)
    # ver = [tuple(i[0]) for i in edges]
    # print(ver)
    tree = [edges[0][0]]
    ver.pop(0)
    for verx in ver:  # comp=m*n^2 == bad
        tree.append(verx[0])
        l = list_of_sets.count(set())
        l_copy = list_of_sets.count(set())
        reserved_1 = []
        for i in range(len(list_of_sets)):
            if (tree[-1][0] in list_of_sets[i] and tree[-1][1] not in list_of_sets[i]) or (tree[-1][0] not in list_of_sets[i] and tree[-1][1] in list_of_sets[i]):
                reserved_1.append(list_of_sets[i])
                list_of_sets[i] = set()
                if len(reserved_1) == 2:
                    list_of_sets[i] = reserved_1[0].union(reserved_1[1])
                    l = list_of_sets.count(set())
                    break

                # for j in range(len(list_of_sets)):
                #     if tree[-1][1] in list_of_sets[j] and i != j:
                #         list_of_sets[i] = list_of_sets[i].union(
                #             list_of_sets[j])
                #         list_of_sets[j] = set()
                #         l = list_of_sets.count(set())
                #         break
        if l == l_copy:
            tree.pop(-1)
        # print(tree)
    # print(list_of_sets)
    # tree.pop(0)
    # print(list_of_sets)
    return tree


if __name__ == "__main__":
    iterations=100
    time_taken = 0
    graph=gnp_random_connected_graph(100,1)
    for _ in tqdm(range(iterations)):
        start = time.time()
        crascal(graph)
        end = time.time()
        time_taken += (end-start)
    print(time_taken)
    # print(len(tree))
    print(time_taken/iterations)


# print(crascal(([(0, 3), (0, 4), (0, 5), (1, 5), (1, 2), (1, 4),
#       (2, 3), (2, 5), (3, 5), (4, 5)], [1, 4, 3, 8, 10, 7, 5, 9, 2, 15])))
