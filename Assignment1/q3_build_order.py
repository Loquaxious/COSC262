def build_order(dependencies):
    """Takes a descrtiption of dependecies between a number of programs and 
    returns a valid order for the build process"""
    
    adj_lst = adjacency_list(dependencies)
    n = len(adj_lst)
    state = ['U' for _ in range(n)]
    stack = []
    for i in range(n):
        if state[i] != 'P':
            dfs_loop(adj_lst, i, state, stack)
    stack.reverse()
    return stack
    
    
    
def dfs_loop(adj_list, start, state, stack):
    """The main loop of DFS"""
    for v in adj_list[start]:
        v = int(v[0])
        if state[v] == 'U':
            state[v] = 'D'
            dfs_loop(adj_list, v, state, stack)
    state[start] = 'P'
    stack.append(start)
    
    
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

dependencies = """\
D 2
0 1
"""

print(build_order(dependencies))

dependencies = """\
D 3
1 2
0 2
"""

print(build_order(dependencies) in [[0, 1, 2], [1, 0, 2]])

dependencies = """\
D 3
"""
# any permutation of 0, 1, 2 is valid in this case.
solution = build_order(dependencies)
if solution is None:
    print("Wrong answer!")
else:
    print(sorted(solution))
    
depen = """\
D 5
0 2
1 2
2 4
2 3
"""
print(build_order(depen))