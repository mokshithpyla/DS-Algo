# Your task is to complete this function
# Function should return True/False or 1/0
# Graph(graph) is a defaultict of type List
# n is no of Vertices
# https://practice.geeksforgeeks.org/problems/detect-cycle-in-a-directed-graph/1


def cyclic(i, n, graph, visited, inTheCall):
    visited[i] = True
    inTheCall[i] = True
    for j in range(len(graph[i])):
        if not visited[graph[i][j]] and cyclic(graph[i][j], n, graph, visited, inTheCall):
            return True
        elif inTheCall[graph[i][j]]:
            return True
    inTheCall[i] = False
    return False

def isCyclic(n, graph):
    # Code here
    visited = {}
    inTheCall = {}
    for _ in range(n):
        visited[_] = False
        inTheCall[_] = False
    for i in range(n):
        if not visited[i]:
            if (cyclic(i, n, graph, visited, inTheCall)):
                return True
    return False