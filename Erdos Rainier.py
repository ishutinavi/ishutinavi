import networkx as nx

n = 15
p = 0.85
G = nx.erdos_renyi_graph(n, p)
a = 0
for i in G.nodes():
    a = a + G.degree(i)
print(f'Средняя степень вершин графа: {float(a)/len(G.nodes())}')
print(f'Теоретическая величина средней степень вершин графа: {(n-1)/p}')