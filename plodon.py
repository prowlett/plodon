import networkx as nx
from math import comb
# import matplotlib.pyplot as plt

def countpaths(A):
    """
    Sums across vertices the number of nodes choose 2.
    """
    paths = 0
    for i in list(A.nodes):
        paths += comb(A.degree[i],2)
    return paths

def add_edge_if(M,a,b,nodes):
    """
    nodes is a list of node numbers. Function adds an edge to M from a to b only if a and b and at least one of nodes is in the graph.
    """
    if M.has_node(a) and M.has_node(b):
        if not nodes or M.has_node(nodes[0]) or M.has_node(nodes[1]):
            M.add_edge(a,b)
            return True
        return False

def build_edges(F):
    """
    Adds edges to F if they won't lead to crossings.
    """
    add_edge_if(F,1,2,[])
    add_edge_if(F,1,4,[])
    add_edge_if(F,1,5,[2,4])

    add_edge_if(F,2,3,[])
    add_edge_if(F,2,4,[1,5])
    add_edge_if(F,2,5,[])
    add_edge_if(F,2,6,[3,5])

    add_edge_if(F,3,5,[2,6])
    add_edge_if(F,3,6,[])

    add_edge_if(F,4,5,[])
    add_edge_if(F,4,7,[])
    add_edge_if(F,4,8,[7,5])

    add_edge_if(F,5,6,[])
    add_edge_if(F,5,7,[4,8])
    add_edge_if(F,5,8,[])
    add_edge_if(F,5,9,[8,6])

    add_edge_if(F,6,8,[5,9])
    add_edge_if(F,6,9,[])

    add_edge_if(F,7,8,[])

    add_edge_if(F,8,9,[])

G = nx.Graph()

for i in range(1,10):
    G.add_node(i)

build_edges(G)

# nx.draw(G)
# plt.show()

# finds potential first paths and puts them in paths1
paths1 = []
for m in list(G.nodes):
    for n in list(G.adj[m]): # n is adjacent to m
        for o in list(G.adj[n]): # o is adjacent to n
            if m!=o: # don't re-visit node
                thislist = [m,n,o]
                thislistr = [o,n,m] # don't count same thing the other way round
                if thislist not in paths1 and thislistr not in paths1:
                    # print(thislist)
                    paths1.append(thislist)

total_paths = 0

for i in range(len(paths1)):
    path2 = nx.Graph()
    nodes = [x for x in range(1,10)]
    for n in paths1[i]:
        nodes.remove(n)
    # print(nodes)
    path2.add_nodes_from(nodes)
    # print(path2.number_of_nodes())
    build_edges(path2)

    print(f"{i+1}. path 1 is {paths1[i][0]}-{paths1[i][1]}-{paths1[i][2]}; {countpaths(path2)} options for path 2")
    
    # nx.draw(path2)
    # plt.show()

    total_paths += countpaths(path2)

print(f"Total: {total_paths}")