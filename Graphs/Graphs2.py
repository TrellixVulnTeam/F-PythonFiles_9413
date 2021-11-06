import copy
import pickle

import networkx as nx


class person():
    def __init__(self, name, surname):
        self.__name = name
        self.__surname = surname

    def getName(self):
        return self.__name


p1 = person("Kevin", "Bacon")
p2 = person("Tom", "Hanks")
p3 = person("Meg", "Ryan")
p4 = person("Parker", "Posey")
p5 = person("Lisa", "Kudrow")

G = nx.DiGraph()

G.add_node(p1)
G.add_node(p2)

# Añadir aristas
G.add_edge(p1, p2)
G.add_edge(p1, p3)
G.add_edges_from([(p2, p3), (p2, p4)])
G.add_edges_from([(p4, p3), (p4, p5)])

print("nodes " + str(len(G.nodes)))

subG = nx.DiGraph()
subG.add_nodes_from(G.nodes)
subG.add_edges_from(G.edges)

def generateSubgraph(originalGraph,removingNodes:[]):
    subG = nx.DiGraph()
    subG.add_nodes_from(originalGraph.nodes)
    subG.add_edges_from(originalGraph.edges)
    for i in removingNodes:
        subG.remove_node(i)
    return subG

def printPath(path):
    for i in path:
        print(i.getName())
print("                     G")
print(printPath(G.nodes))

print("                     subG")
print(printPath(generateSubgraph(G,[p2,p3])))


def write(data: []):

    binaryFile = open("binaryFile", "wb")

    pickle.dump(data, binaryFile)

    binaryFile.close()

    del binaryFile

    for i in data:
        print(i)

write([G,subG])