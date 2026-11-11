
# Create Graph
def create_graph():
    graph = {
        "N": ["A", "L"],
        "A": ["N", "B", "E"],
        "B": ["A"],
        "L": ["N"],
        "E": ["A"]
    }

    return graph


# BFS - Visit level by level
def bfs(graph, start):
    queue = [start]
    visited = []
    result = []

    while queue:
        vertex = queue.pop(0)

        if vertex not in visited:
            visited.append(vertex)
            result.append(vertex)

            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)

    return result


# DFS - Visit deeply before going back
def dfs(graph, start, visited=None):
    if visited is None:
        visited = []

    visited.append(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

    return visited


# Main Program
graph = create_graph()

print("GRAPH USING NABLE")
print("BFS:", " -> ".join(bfs(graph, "N")))
print("DFS:", " -> ".join(dfs(graph, "N")))
