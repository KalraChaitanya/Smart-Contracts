import networkx as nx
import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(20,20))
G=nx.Graph()
G.add_edge(1,0 ,color='r',weight=2)
G.add_edge(2,0,color='k',weight=1)
G.add_edge(3,1,color='k',weight=1)
G.add_edge(5,3,color='k',weight=1)
G.add_edge(4,3,color='k',weight=1)
G.add_edge(6,4,color='k',weight=1)
G.add_edge(7,6 ,color='r',weight=2)
G.add_edge(8,6,color='k',weight=1)
G.add_edge(9,7 ,color='r',weight=2)
G.add_edge(10,7,color='k',weight=1)
G.add_edge(11,7,color='k',weight=1)
G.add_edge(13,9,color='k',weight=1)
G.add_edge(12,7,color='k',weight=1)
G.add_edge(14,12,color='k',weight=1)
G.add_edge(16,14,color='k',weight=1)
G.add_edge(15,14,color='k',weight=1)
G.add_edge(17,15,color='k',weight=1)
G.add_edge(18,15,color='k',weight=1)
G.add_edge(19,15,color='k',weight=1)
colors = nx.get_edge_attributes(G,'color').values() 
weights = nx.get_edge_attributes(G,'weight').values()
nx.draw(G,with_labels = True, arrows=True, pos=nx.spring_layout(G), edge_color=colors, width=list(weights))
import matplotlib.pyplot as plt
plt.savefig('blockchaingraph19.svg', format='svg', dpi=1200)