from search import bf_search, df_search


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
print("BFS Search from A to F:", bf_search(graph, 'A', 'X'))
print("DFS Search from A to F:", df_search(graph, 'A', 'F'))