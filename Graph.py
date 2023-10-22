# Najam ul Hassan
# sp21-bcs-065
# Graph Theory
#


class Node:
    def __init__(self, state, parent, actions, totalcost):
        self.state = state
        self.parent = parent
        self.actions = actions
        self.totalcost = totalcost


graph = {
    "A": Node("A", None, ["B", "C", "C"], None),
    "B": Node("B", None, ["D", "A"], None),
    "C": Node("C", None, ["A", "F", "G"], None),
    "D": Node("D", None, ["B", "E"], None),
    "E": Node("E", None, ["D", "A"], None),
    "G": Node("G", None, ["C"], None),
    "F": Node("F", None, ["C"], None),
}


romania_TSP = {
    "Arad": Node("Arad", None, ["Zerind", "Sibiu", "Timisoara"], None),
    "Zerind": Node("Zerind", None, ["Arad", "Oradea"], None),
    "Oradea": Node("Oradea", None, ["Zerind", "Sibiu"], None),
    "Sibiu": Node("Sibiu", None, ["Arad", "Oradea", "Fagaras", "Rimnicu Vilcea"], None),
    "Timisoara": Node("Timisoara", None, ["Arad", "Lugoj"], None),
    "Lugoj": Node("Lugoj", None, ["Timisoara", "Mehadia"], None),
    "Mehadia": Node("Mehadia", None, ["Lugoj", "Drobeta"], None),
    "Drobeta": Node("Drobeta", None, ["Mehadia", "Craiova"], None),
    "Craiova": Node("Craiova", None, ["Drobeta", "Rimnicu Vilcea", "Pitesti"], None),
    "Rimnicu Vilcea": Node(
        "Rimnicu Vilcea", None, ["Sibiu", "Craiova", "Pitesti"], None
    ),
    "Fagaras": Node("Fagaras", None, ["Sibiu", "Bucharest"], None),
    "Pitesti": Node("Pitesti", None, ["Rimnicu Vilcea", "Craiova", "Bucharest"], None),
    "Bucharest": Node(
        "Bucharest", None, ["Fagaras", "Pitesti", "Giurgiu", "Urziceni"], None
    ),
    "Giurgiu": Node("Giurgiu", None, ["Bucharest"], None),
    "Urziceni": Node("Urziceni", None, ["Bucharest", "Hirsova", "Vaslui"], None),
    "Hirsova": Node("Hirsova", None, ["Urziceni", "Eforie"], None),
    "Eforie": Node("Eforie", None, ["Hirsova"], None),
    "Vaslui": Node("Vaslui", None, ["Urziceni", "Iasi"], None),
    "Iasi": Node("Iasi", None, ["Vaslui", "Neamt"], None),
    "Neamt": Node("Neamt", None, ["Iasi"], None),
}


def BFS(graph, start, goal):
    queue = []
    visited = []
    queue.append(start)
    visited.append(start)
    path = []
    while queue:
        current = queue.pop(0)
        path.append(current)
        # print the exact path
        print(current)
        if current == goal:
            return path
        for neighbor in graph[current].actions:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.append(neighbor)
    return path


def BFS2(graph, start, goal):
    queue = []
    visited = []
    queue.append(start)
    visited.append(start)

    while queue:
        current = queue.pop(0)
        if current == goal:
            return actionSequence(graph, start, goal)  # Change to start here
        for neighbor in graph[current].actions:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.append(neighbor)
                graph[neighbor].parent = current


def DFS(graph, start, goal):
    stack = []
    visited = []
    stack.append(start)
    visited.append(start)

    while stack:
        current = stack.pop()

        # print the exact path
        print(current)
        if current == goal:
            return actionSequence(graph, start, goal)
        for neighbor in graph[current].actions:
            if neighbor not in visited:
                stack.append(neighbor)
                visited.append(neighbor)
                graph[neighbor].parent = current


def actionSequence(graph, start, goal):
    solution = [goal]
    current = goal
    while current != start:
        currentParent = graph[current].parent
        solution.append(currentParent)
        current = currentParent
    solution.reverse()
    return solution


# Testing the code
print(BFS2(graph, "D", "F"))

print(DFS(romania_TSP, "Bucharest", "Arad"))
