"""
Module implementing Kruskal's algorithm for minimal spanning tree generation
"""


def generate_mst_kruskal(graph):
    """
    Generate minimum spanning tree
    """
    vertexes = graph[0]
    weights = graph[1]
    edges = list(vertexes.edges())
    for i in range(len(edges)):
        edges[i] = [edges[i], weights[i]]
    set_of_vertex = set()
    for item in edges:
        for number in item[0]:
            set_of_vertex.add(number)
    list_of_sets = []
    for item in set_of_vertex:
        list_of_sets.append({item})
    edges = sorted(edges, key=lambda x: x[1])
    ver = {tuple(i[0]) for i in edges}
    # new_set=set()
    tree = [edges[0][0]]
    edges.pop(0)
    # print(set_of_vertex )
    for verx in ver: #comp=m*n^2
        tree.append(verx)
        l = list_of_sets.count(set())
        l_copy = list_of_sets.count(set())
        for i in range(len(list_of_sets)):
            if tree[-1][0] in list_of_sets[i] and tree[-1][1] not in list_of_sets[i]:
                for j in range(len(list_of_sets)):
                    if tree[-1][1] in list_of_sets[j] and i != j:
                        list_of_sets[i] = list_of_sets[i].union(
                            list_of_sets[j])
                        list_of_sets[j] = set()
                        l = list_of_sets.count(set())
                        break
                break
        if l == l_copy:
            tree.pop(-1)
    # print(list_of_sets)
    tree.pop(0)
    # print(list_of_sets)
    return tree
