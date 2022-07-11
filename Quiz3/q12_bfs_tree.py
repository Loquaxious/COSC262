import collections
from q2_adjacency_list import adjacency_list

def bfs_tree(adj_list, start):
    """Takes a adjacency list and a starting vertex then 
    performs Breadth-first search and returns the parent
    array"""
    n = len(adj_list) 
    state = ['U' for _ in range(n)]
    parent = [None for _ in range(n)]
    q = collections.deque()
    state[start] = 'D'
    q.append(start)
    return bfs_loop(adj_list, q, state, parent)
    

def bfs_loop(adj_list, queue, state, parent):
    """Main loop of BFS"""
    while (len(queue) != 0):
        u = int(queue.popleft())
        for v in adj_list[u]:
            v = int(v[0])
            if state[v] == 'U':
                state[v] == 'D'
                if parent[v] == None:
                    parent[v] = u
                queue.append(v)
        state[u] = 'P'
    return parent


## an undirected graph

#adj_list = [
    #[(1, None)],
    #[(0, None), (2, None)],
    #[(1, None)]
#]

#print(bfs_tree(adj_list, 0))
#print(bfs_tree(adj_list, 1))

## a directed graph (note the asymmetrical adjacency list)

#adj_list = [
#[(1, None)],
#[]
#]

#print(bfs_tree(adj_list, 0))
#print(bfs_tree(adj_list, 1))

#graph_string0 = """\
#D 2
#0 1
#"""

#print(bfs_tree(adjacency_list(graph_string0), 0))

#graph_string1 = """\
#D 2
#0 1
#1 0
#"""

#print(bfs_tree(adjacency_list(graph_string1), 1))

##graph from the textbook example
#graph_string2 = """\
#U 7
#1 2
#1 5
#1 6
#2 3
#2 5
#3 4
#4 5
#"""

#print(bfs_tree(adjacency_list(graph_string2), 1))

#graph_string3 = """\
#D 2 W
#0 1 99
#"""

#print(bfs_tree(adjacency_list(graph_string3), 0))

	
# an undirected graph

adj_list = [
    [(3, None), (1, None)],
    [(0, None), (2, None)],
    [(3, None), (1, None)],
    [(0, None), (2, None)]
]

for s in range(4):
    print(bfs_tree(adj_list, s))
    
# graph from the textbook example
graph_string = """\
U 7
1 2
1 5
1 6
2 3
2 5
3 4
4 5
"""

print(bfs_tree(adjacency_list(graph_string), 1))

graph_string = """\
D 7
0 1
3 4
5 6
4 5
3 5
"""

print(bfs_tree(adjacency_list(graph_string), 0))
print(bfs_tree(adjacency_list(graph_string), 1))
print(bfs_tree(adjacency_list(graph_string), 3))
print(bfs_tree(adjacency_list(graph_string), 4))

graph_string = """\
U 4
0 1
1 2
2 3
3 0
"""

print(bfs_tree(adjacency_list(graph_string), 0))