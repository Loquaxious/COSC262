from adjacency_list import adjacency_list

def transpose(adj_list):
    """Takes and adjacency list and returns the reverse of the adjacency list"""
    
    result = [[] for _ in range(len(adj_list))]
    
    for vertex in range(len(adj_list)):
        for edge in adj_list[vertex]:
            result[edge[0]].append((vertex, edge[1]))
    
    return result

#graph_string = """\
#D 3
#0 1
#1 0
#0 2
#"""

#graph_adj_list = adjacency_list(graph_string)
#graph_transposed_adj_list = transpose(graph_adj_list)
#for i in range(len(graph_transposed_adj_list)):
    #print(i, sorted(graph_transposed_adj_list[i]))
    
#graph_string = """\
#D 3 W
#0 1 7
#1 0 -2
#0 2 0
#"""

#graph_adj_list = adjacency_list(graph_string)
#graph_transposed_adj_list = transpose(graph_adj_list)
#for i in range(len(graph_transposed_adj_list)):
    #print(i, sorted(graph_transposed_adj_list[i]))
    
## It should also work undirected graphs.
## The output will be the same as input.

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

#graph_adj_list = adjacency_list(graph_string)
#graph_transposed_adj_list = transpose(graph_adj_list)
#for i in range(len(graph_transposed_adj_list)):
    #print(i, sorted(graph_transposed_adj_list[i]))
    
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

graph_adj_list = adjacency_list(graph_string)
graph_transposed_adj_list = transpose(graph_adj_list)
for i in range(len(graph_transposed_adj_list)):
    print(i, sorted(graph_transposed_adj_list[i]))