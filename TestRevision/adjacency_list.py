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
        
        
#graph_string = """\
#D 3
#0 1
#1 0
#0 2
#"""
#print(adjacency_list(graph_string)) 

#graph_string = """\
#D 3 W
#0 1 7
#1 0 -2
#0 2 0
#"""
#print(adjacency_list(graph_string))

from pprint import pprint

## undirected graph in the textbook example
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

#pprint(adjacency_list(graph_string))

#graph_string = """\
#U 17
#1 2
#1 15
#1 6
#12 13
#2 15
#13 4
#4 5
#"""

#pprint(adjacency_list(graph_string))
