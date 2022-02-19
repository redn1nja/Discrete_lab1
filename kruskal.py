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
    edges = dict(zip(edges, weights))
    list_of_sets=[{i} for i in list(graph.nodes())]
    # print(list_of_sets)
    ver = dict(sorted(edges.items(), key = lambda x: x[1]))
    # print(ver)
    tree=[]
    # list_of_sets_2=list_of_sets
    # print(ver)
    for verx in ver:
        l=0
        l_copy= 0
        reserved_1 = []
        for i in range(len(list_of_sets)):
            if (verx[0] in list_of_sets[i] and verx[1] not in list_of_sets[i]) or (verx[0] not in list_of_sets[i] and verx[1] in list_of_sets[i]):
                reserved_1.append(list_of_sets[i])
                list_of_sets[i] = set()
                if len(reserved_1) == 2:
                    list_of_sets[i] = reserved_1[0].union(reserved_1[1])
                    l = 1
                    break
        if l != l_copy:
            tree.append(verx)
        if len(tree)==(len(list_of_sets)-1):
            break

    result = nx.Graph()
    result.add_nodes_from(list(graph.nodes()))
    edge_dict = dict(edges)
    result.add_edges_from([(*edge, {"weight": edge_dict[edge]}) for edge in tree])
    return result

