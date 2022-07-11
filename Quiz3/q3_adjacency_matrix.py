def adjacency_matrix(graph_str):
    """Takes the textual representation of a graph and
    returns its corresponding adjacency matrix"""
    char_lst = []
    split_str = graph_str.splitlines()
    for line in split_str:
        char_lst.append(line.split())
    
    if char_lst[0][0] == "D":
        result = directed_adj_mat(char_lst)
    elif char_lst[0][0] == "U":
        result = undirected_adj_mat(char_lst)
    else:
        result = []
    
    return result 


def directed_adj_mat(char_lst):
    """Returns a directed adjacency matrix"""
    vertices = int(char_lst[0][1])
    result = [[0 for _ in range(vertices)] for _ in range(vertices)]
    
    if len(char_lst[0]) == 3:
        weighted = True
        result = [[None for _ in range(vertices)] for _ in range(vertices)]
    else:
        weighted = False
        result = [[0 for _ in range(vertices)] for _ in range(vertices)]
        
    for edge in char_lst[1:]:
        if weighted:
            result[int(edge[0])][int(edge[1])] = int(edge[2])
        else:
            result[int(edge[0])][int(edge[1])] = 1
    
    return result

def undirected_adj_mat(char_lst):
    """Returns a undirected adjacency matrix"""
    vertices = int(char_lst[0][1])
    result = [[0 for _ in range(vertices)] for _ in range(vertices)]
    
    if len(char_lst[0]) == 3:
        weighted = True
        result = [[None for _ in range(vertices)] for _ in range(vertices)]
    else:
        weighted = False
        result = [[0 for _ in range(vertices)] for _ in range(vertices)]
        
    for edge in char_lst[1:]:
        if weighted:
            result[int(edge[0])][int(edge[1])] = int(edge[2])
            result[int(edge[1])][int(edge[0])] = int(edge[2])
        else:
            result[int(edge[0])][int(edge[1])] = 1
            result[int(edge[1])][int(edge[0])] = 1
    
    return result    


graph_string = """\
D 3
0 1
1 0
0 2
"""

print(adjacency_matrix(graph_string))   

graph_string = """\
D 3 W
0 1 7
1 0 -2
0 2 0
"""
print(adjacency_matrix(graph_string))

from pprint import pprint

graph_string = """\
U 7
1 2
1 5
1 6
3 4
0 4
4 5
"""

pprint(adjacency_matrix(graph_string))

graph_string = """\
U 17
1 2
1 15
1 6
12 13
2 15
13 4
4 5
"""

pprint(adjacency_matrix(graph_string))