from q2_adjacency_list import adjacency_list

def dfs_tree(adj_list, start):
    """Takes an adjacency list and a starting vertex, 
    performs depth-first search and returns the parent array"""
    n = len(adj_list) 
    state = ['U' for _ in range(n)]
    parent = [None for _ in range(n)]
    state[start] = 'D'
    dfs_loop(adj_list, start, state, parent)
    return parent


def dfs_loop(adj_list, start, state, parent):
    """The main loop of DFS"""
    for v in adj_list[start]:
        v = int(v[0])
        if state[v] == 'U':
            state[v] = 'D'
            parent[v] = start
            dfs_loop(adj_list, v, state, parent)
    state[start] = 'P'
    
## an undirected graph

#adj_list = [
    #[(1, None), (2, None)],
    #[(0, None), (2, None)],
    #[(0, None), (1, None)]
#]

#print(dfs_tree(adj_list, 0))
#print(dfs_tree(adj_list, 1))
#print(dfs_tree(adj_list, 2))

## a directed graph (note the asymmetrical adjacency list)

#adj_list = [
#[(1, None)],
#[]
#]

#print(dfs_tree(adj_list, 0))
#print(dfs_tree(adj_list, 1))

## graph from the textbook example
#graph_string = """\
#U 7
#1 2
#1 5
#1 6
#2 3
#2 5
#3 4
#4 5
#"""

#print(dfs_tree(adjacency_list(graph_string), 1))

#gstring = """\
#U 4
#2 3
#2 1
#0 3
#1 0
#"""

#print(dfs_tree(adjacency_list(gstring), 0))