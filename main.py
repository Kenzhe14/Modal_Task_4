import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms.community import girvan_newman

# 1. Create a directed graph (~500 nodes)
G = nx.gnp_random_graph(500, 0.01, directed=True)

# 2. Compute metrics
degree = dict(G.degree())
betweenness = nx.betweenness_centrality(G)
clustering = nx.clustering(G.to_undirected())

# 3. Detect communities
communities_gen = girvan_newman(G.to_undirected())
communities = [list(c) for c in next(communities_gen)]

# 4. Visualize spring layout (Figure 5)
pos = nx.spring_layout(G, seed=42)
plt.figure(figsize=(8,8))
nx.draw(G, pos, node_color='skyblue', edge_color='gray', node_size=50, arrowsize=10, with_labels=False)
plt.title("Figure 5 – Spring layout")
plt.show()

# 5. Highlight top-5 nodes by betweenness (Figure 6)
top_nodes = sorted(betweenness, key=betweenness.get, reverse=True)[:5]
colors = ['red' if n in top_nodes else 'skyblue' for n in G.nodes()]
plt.figure(figsize=(8,8))
nx.draw(G, pos, node_color=colors, edge_color='gray', node_size=50, arrowsize=10, with_labels=False)
plt.title("Figure 6 – Top nodes highlighted")
plt.show()

# 6. Community structure (Figure 4)
comm_colors = ['red','green','blue','orange','purple','yellow']
node_colors = []
for node in G.nodes():
    for i, comm in enumerate(communities):
        if node in comm:
            node_colors.append(comm_colors[i % len(comm_colors)])
plt.figure(figsize=(8,8))
nx.draw(G, pos, node_color=node_colors, edge_color='gray', node_size=50, arrowsize=10, with_labels=False)
plt.title("Figure 4 – Communities")
plt.show()

# 7. Compare layouts (Figure 9)
plt.figure(figsize=(12,6))
plt.subplot(1,2,1)
nx.draw(G, pos, node_color='skyblue', edge_color='gray', node_size=50, arrowsize=10, with_labels=False)
plt.title("Spring Layout")
plt.subplot(1,2,2)
pos_circ = nx.circular_layout(G)
nx.draw(G, pos_circ, node_color='skyblue', edge_color='gray', node_size=50, arrowsize=10, with_labels=False)
plt.title("Circular Layout")
plt.show()

# 8. Degree distribution histogram (Figure 7)
plt.figure(figsize=(6,4))
plt.hist(list(degree.values()), bins=30, color='skyblue', edgecolor='black')
plt.xlabel("Degree")
plt.ylabel("Number of nodes")
plt.title("Figure 7 – Degree distribution")
plt.show()

# 9. Print top nodes by centrality (Figure 8)
top_centrality = sorted(betweenness.items(), key=lambda x: x[1], reverse=True)[:10]
print("Figure 8 – Top nodes by betweenness:")
print("Node\tBetweenness\tDegree")
for node, score in top_centrality:
    print(f"{node}\t{score:.4f}\t{degree[node]}")
