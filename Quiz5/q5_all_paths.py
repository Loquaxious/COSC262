from adjacency_list import adjacency_list

def all_paths(adj_list, source, destination):
    """Takes the adjacency list of a graph, a source vertex (int), and a 
    destination vertex (int) and returns a list of all simple paths (all 
    possible without a cycle) from the sorce vertex to the destination
    vertex"""
    results = []
    dfs_backtrack((source,), adj_list, destination, results)
    return results


def dfs_backtrack(candidate, adj_list, destination, output_data):
    if should_prune(candidate):
        return
    if is_solution(candidate, destination):
        add_to_output(candidate, output_data)
    else:
        for child_candidate in children(candidate, adj_list):
            dfs_backtrack(child_candidate, adj_list, destination, output_data)


def is_solution(candidate_path, destination):
    """Returns True if the candidate is complete solution"""
    return destination in candidate_path


def children(candidate_path, adj_list):
    """Returns a collestion of candidates that are the children of the given
    candidate."""
    children = []
    n = len(candidate_path)
    
    for edge in adj_list[candidate_path[n-1]]:
        if edge[0] not in candidate_path:
            children.append(candidate_path + (edge[0],))
        
    return children
     
    
def add_to_output(candidate, output_data):
    output_data.append(candidate)

    
def should_prune(candidate):
    return False


triangle_graph_str = """\
U 3
0 1
1 2
2 0
"""

adj_list = adjacency_list(triangle_graph_str)
print(sorted(all_paths(adj_list, 0, 2)))
print(all_paths(adj_list, 1, 1))

graph_str = """\
U 5
0 2
1 2
3 2
4 2
1 4
"""

adj_list = adjacency_list(graph_str)
print(sorted(all_paths(adj_list, 0, 1)))

from pprint import pprint

# graph used in tracing bfs and dfs
graph_str = """\
D 7
6 0
6 5
0 1
0 2
1 2
1 3
2 4
2 5
4 3
5 4
"""

adj_list = adjacency_list(graph_str)
pprint(sorted(all_paths(adj_list, 6, 3)))