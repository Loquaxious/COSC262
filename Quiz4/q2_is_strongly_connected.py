from adjacency_list import adjacency_list

def is_strongly_connected(adj_list):
    """Takes and adjacency list (with at least one vertex) and returns 
    true if the graph is strongly connected"""
    state1 = dfs_tree(adj_list)
    if 'U' in state1:
        return False
    else:
        trnspse = transpose(adj_list)
        state2 = dfs_tree(trnspse)
        if 'U' in state2:
            return False
        else:
            return True
    
def dfs_tree(adj_list, start=0):
    """Takes an adjacency list and a starting vertex, 
    performs depth-first search and returns the state array"""
    n = len(adj_list) 
    state = ['U' for _ in range(n)]
    parent = [None for _ in range(n)]
    state[start] = 'D'
    dfs_loop(adj_list, start, state, parent)
    return state


def dfs_loop(adj_list, start, state, parent):
    """The main loop of DFS"""
    for v in adj_list[start]:
        v = int(v[0])
        if state[v] == 'U':
            state[v] = 'D'
            parent[v] = start
            dfs_loop(adj_list, v, state, parent)
    state[start] = 'P'   
    
    
def transpose(adj_list):
    """Takes and adjacency list and returns the reverse of the adjacency list"""
    
    result = [[] for _ in range(len(adj_list))]
    
    for vertex in range(len(adj_list)):
        for edge in adj_list[vertex]:
            result[edge[0]].append((vertex, edge[1]))
    
    return result

graph_string = """\
D 3
0 1
1 0
0 2
"""

print(is_strongly_connected(adjacency_list(graph_string)))

graph_string = """\
D 3
0 1
1 2
2 0
"""

print(is_strongly_connected(adjacency_list(graph_string)))

graph_string = """\
D 4
0 1
1 2
2 0
"""

print(is_strongly_connected(adjacency_list(graph_string)))

# Since we are passing an adjacency list to your algorithm,
# it will see an un directed graph as a directed one where each
# undirected edge appears as two directed edges.

graph_string = """\
U 5
2 4
3 1
0 4
2 1
"""

print(is_strongly_connected(adjacency_list(graph_string)))