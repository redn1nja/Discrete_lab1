"""
Module implementing Kruskal's algorithm for minimum spanning tree generation
"""
import networkx as nx


def generate_mst_kruskal(graph: nx.Graph) -> nx.Graph:
    """
    Generate minimum spanning tree using Kruskal's algorithm
    """
    # edges = graph[0]

    # vertexes = graph[0]
    weights = [data[2]["weight"] for data in graph.edges(data=True)]
    edges = list(graph.edges())
    edges = list(zip(edges, weights))
    # print(edges)
    # set_of_vertex = set()
    # for item in edges:
    #     for number in item[0]:
    #         set_of_vertex.add(number)
    # list_of_sets = []
    # for item in set_of_vertex:
    #     list_of_sets.append({item})
    list_of_sets = [{i} for i in list(graph.nodes())]
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
    result = nx.Graph()
    result.add_nodes_from(list(graph.nodes()))
    edge_dict = dict(edges)
    result.add_edges_from([(*edge, {"weight": edge_dict[edge]}) for edge in tree])
    return result
