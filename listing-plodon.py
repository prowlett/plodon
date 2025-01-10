import networkx as nx
from math import comb

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

letter_no = 0

letters = []

for i in range(len(paths1)):
    # make the subgraph that's still viable after this path 1
    nodes = [x for x in range(1,10)]
    for n in paths1[i]:
        nodes.remove(n)
    H = nx.Graph()
    H.add_nodes_from(nodes)
    build_edges(H)

    # find potential second paths and put them in paths2
    paths2 = []
    for m in list(H.nodes):
        for n in list(H.adj[m]): # n is adjacent to m
            for o in list(H.adj[n]): # o is adjacent to n
                if m!=o: # don't re-visit node
                    thislist = [m,n,o]
                    thislistr = [o,n,m] # don't count same thing the other way round
                    if thislist not in paths2 and thislistr not in paths2:
                        # print(thislist)
                        paths2.append(thislist)

    # output all the path 1, path 2 pairs found
    for p in paths2:
        if f"{paths1[i][0]}-{paths1[i][1]}-{paths1[i][2]}-{p[0]}-{p[1]}-{p[2]}" not in letters and f"{p[0]}-{p[1]}-{p[2]}-{paths1[i][0]}-{paths1[i][1]}-{paths1[i][2]}" not in letters: # check we haven't done this one before in reverse
            letters.append(f"{paths1[i][0]}-{paths1[i][1]}-{paths1[i][2]}-{p[0]}-{p[1]}-{p[2]}")
            letter_no += 1
            print(f"Letter {letter_no}: path 1 {paths1[i][0]}-{paths1[i][1]}-{paths1[i][2]}; path 2 {p[0]}-{p[1]}-{p[2]}")
