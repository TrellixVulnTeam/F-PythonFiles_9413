import networkx as nx

Grafo = nx.DiGraph()

Grafo.add_edge(2,"E")
Grafo.add_edge("E",2)
Grafo.add_edge("E","I")
Grafo.add_edge("I","U")
Grafo[2]["E"]["price"] = 3
Grafo["E"][2]["price"] = 6
print(Grafo.edges)
print(Grafo.nodes)
print(Grafo.get_edge_data(2,"E"))
print(Grafo.get_edge_data("E",2))

