import networkx as nx

G = nx.Graph()
G.add_edges_from([(0, 1), (0, 2), (0, 3)])  # Узел 0 наиболее задействован
centrality = nx.degree_centrality(G)
for n in centrality:
  print(f'с( {n}):{centrality[n]:.2f}')
nx.draw(G, with_labels = True)