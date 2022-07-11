import collections

def bubbles(physical_contact_info):
    """Takes physcial contact information about a group of people and determines the bubbles"""
    
    adj_lst = adjacency_list(physical_contact_info)
    return connected_components(adj_lst)
    
    
def connected_components(adj_lst):
    """Takes and adjacency list and returns all components of the graph"""
    
    n = len(adj_lst)
    state = ['U' for _ in range(n)]
    q = collections.deque()
    components = []
    
    for i in range(n):
        if state[i] == 'U':
            prev = state[:]
            state[i] = 'D'
            q.append(i)
            state = bfs_loop(adj_lst, q, state)
            new_comp = []
            for j in range(n):
                if state[j] != prev[j]:
                    new_comp.append(j)
            components.append(new_comp)
    return components
                    


def bfs_loop(adj_list, queue, state):
    """Main loop of BFS"""
    while (len(queue) != 0):
        u = int(queue.popleft())
        for v in adj_list[u]:
            v = int(v[0])
            if state[v] == 'U':
                state[v] == 'D'
                queue.append(v)
        state[u] = 'P'
    return state
            
    
def adjacency_list(graph_str):
    """Takes the textual representation of a graph and returns
    the adjacency list representation"""
    char_lst = []
    split_str = graph_str.splitlines()
    for line in split_str:
        char_lst.append(line.split())
    
    if char_lst[0][0] == "D":
        result = directed_adj_lst(char_lst)
    elif char_lst[0][0] == "U":
        result = undirected_adj_lst(char_lst)
    else:
        result = []
    
    return result 

def directed_adj_lst(char_lst):
    """Returns a directed adjacency list"""
    vertices = int(char_lst[0][1])
    result = [[] for _ in range(vertices)]
    
    if len(char_lst[0]) == 3:
        weighted = True
    else:
        weighted = False
    
    for edge in char_lst[1:]:
        if weighted:
            result[int(edge[0])].append((int(edge[1]), int(edge[2])))
        else:
            result[int(edge[0])].append((int(edge[1]), None))
    
    return result

def undirected_adj_lst(char_lst):
    """Returns a undirected adjacency list"""
    vertices = int(char_lst[0][1])
    result = [[] for _ in range(vertices)]
    
    if len(char_lst[0]) == 3:
        weighted = True
    else:
        weighted = False
    
    for edge in char_lst[1:]:
        if weighted:
            result[int(edge[0])].append((int(edge[1]), int(edge[2])))
            result[int(edge[1])].append((int(edge[0]), int(edge[2])))
        else:
            result[int(edge[0])].append((int(edge[1]), None))
            result[int(edge[1])].append((int(edge[0]), None))
    
    return result  


physical_contact_info = """\
U 2
0 1
"""

print(sorted(sorted(bubble) for bubble in bubbles(physical_contact_info)))

physical_contact_info = """\
U 2
"""

print(sorted(sorted(bubble) for bubble in bubbles(physical_contact_info)))

physical_contact_info = """\
U 7
1 2
1 5
1 6
2 3
2 5
3 4
4 5
"""

print(sorted(sorted(bubble) for bubble in bubbles(physical_contact_info)))

physical_contact_info = """\
U 0
"""

print(sorted(sorted(bubble) for bubble in bubbles(physical_contact_info)))

physical_contact_info = """\
U 1
"""

print(sorted(sorted(bubble) for bubble in bubbles(physical_contact_info)))