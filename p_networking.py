#!/usr/bin/env python
print('----------------python networkx-------------')
import networkx as nx
network = nx.Graph()
nodes = ["hello","world",1,2,3]
for node in nodes:
    network.add_node(node)

network.add_edge("hello","world")
network.add_edge(1,2)
network.add_edge(1,3)

