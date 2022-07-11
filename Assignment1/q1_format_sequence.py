import collections

def format_sequence(converters_info, source_format, destination_format):
    """Takes the video converters information then finds the shortest path from 
     the source video format to desired video format"""
    
    adj_lst = adjacency_list(converters_info)
    prnt_tree = bfs_tree(adj_lst, source_format)
    
    try:
        return tree_path(prnt_tree, source_format, destination_format)
    except TypeError:
        return "No solution!"
        
    
def tree_path(parent, start, destination):
    """Recursive function that finds the shortest path from the root to a destination vertex given a predessor tree"""
    
    if destination == None:
        return 
    elif start == destination: 
        return [start]
    else:
        return tree_path(parent, start, parent[destination]) + [destination] 


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


def adjacency_list(graph_str):
    """Takes the textual representation of a graph and returns
    the adjacency list representation"""
    char_lst = []
    split_str = graph_str.splitlines()
    for line in split_str:
        char_lst.append(line.split())
    
    vertices = int(char_lst[0][1])
    result = [[] for _ in range(vertices)]
    for edge in char_lst[1:]:
        result[int(edge[0])].append((int(edge[1]), None))
        
    return result 



converters_info_str = """\
D 2
0 1
"""

source_format = 0
destination_format = 1

print(format_sequence(converters_info_str, source_format, destination_format))


converters_info_str = """\
D 2
0 1
"""

print(format_sequence(converters_info_str, 1, 1))


converters_info_str = """\
D 2
0 1
"""

print(format_sequence(converters_info_str, 1, 0))


converters_info_str = """\
D 5
1 0
0 2
2 3
1 2
"""

print(format_sequence(converters_info_str, 1, 2))


converters_info_str = """\
D 1
"""

print(format_sequence(converters_info_str, 0, 0))