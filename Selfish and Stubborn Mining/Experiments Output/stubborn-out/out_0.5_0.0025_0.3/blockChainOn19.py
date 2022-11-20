import networkx as nx
import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(20,20))
G=nx.Graph()
G.add_edge(1,0 ,color='r',weight=2)
G.add_edge(4,0,color='k',weight=1)
G.add_edge(2,0,color='k',weight=1)
G.add_edge(9,0,color='k',weight=1)
G.add_edge(12,0,color='k',weight=1)
G.add_edge(7,0,color='k',weight=1)
G.add_edge(5,0,color='k',weight=1)
G.add_edge(11,0,color='k',weight=1)
G.add_edge(3,0,color='k',weight=1)
G.add_edge(10,0,color='k',weight=1)
G.add_edge(8,0,color='k',weight=1)
G.add_edge(6,0,color='k',weight=1)
G.add_edge(13,1,color='k',weight=1)
G.add_edge(14,13,color='k',weight=1)
G.add_edge(15,14 ,color='r',weight=2)
G.add_edge(16,14,color='k',weight=1)
G.add_edge(17,15,color='k',weight=1)
G.add_edge(18,17,color='k',weight=1)
G.add_edge(20,18,color='k',weight=1)
G.add_edge(19,18,color='k',weight=1)
G.add_edge(21,19 ,color='r',weight=2)
G.add_edge(22,20,color='k',weight=1)
G.add_edge(23,20,color='k',weight=1)
G.add_edge(24,21,color='k',weight=1)
G.add_edge(25,24,color='k',weight=1)
G.add_edge(28,25,color='k',weight=1)
G.add_edge(26,25,color='k',weight=1)
G.add_edge(27,25,color='k',weight=1)
G.add_edge(29,28,color='k',weight=1)
G.add_edge(30,29 ,color='r',weight=2)
G.add_edge(31,29,color='k',weight=1)
G.add_edge(32,30 ,color='r',weight=2)
G.add_edge(34,30,color='k',weight=1)
G.add_edge(33,30,color='k',weight=1)
G.add_edge(35,32,color='k',weight=1)
colors = nx.get_edge_attributes(G,'color').values() 
weights = nx.get_edge_attributes(G,'weight').values()
nx.draw(G,with_labels = True, arrows=True, pos=nx.spring_layout(G), edge_color=colors, width=list(weights))
import matplotlib.pyplot as plt
plt.savefig('blockchaingraph19.svg', format='svg', dpi=1200)