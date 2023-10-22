import pandas as pd


class Node:
    def __init__(self, state, parent, actions, totalcost):
        self.state = state
        self.parent = parent
        self.actions = actions
        self.totalcost = totalcost


graph = {
    "S": Node("S", None, [("A", 3), ("B", 7)], 0),
    "A": Node("A", None, [("B", 2), ("D", 9), ("S", 3)], 0),
    "B": Node("B", None, [("A", 2), ("C", 6), ("S", 7)], 0),
    "D": Node("D", None, [("A", 9), ("C", 3), ("F", 13)], 0),
    "C": Node("C", None, [("B", 6), ("D", 3), ("E", 2), ("G", 1)], 0),
    "F": Node("F", None, [("D", 13)], 0),
    "G": Node("G", None, [("C", 1)], 0),
    "E": Node("E", None, [("C", 2)], 0),
}


def actionSequence(graph, start, goal):
    solution = [goal]
    current = goal
    while current != start:
        currentParent = graph[current].parent
        solution.append(currentParent)
        current = currentParent
    solution.reverse()
    return solution


def Uniform_cost_search(graph, start, goal):
    queue = []
    visited = []
    queue.append(start)
    visited.append(start)

    # Create an empty DataFrame to store the search algorithm steps
    columns = ["Current Node", "Queue", "Visited", "Total Cost"]
    data = []
    df = pd.DataFrame(data, columns=columns)

    while queue:
        current = queue.pop(0)

        # Add the current state of the search algorithm to the DataFrame
        queue_str = ", ".join(queue)
        visited_str = ", ".join(visited)
        data.append([current, queue_str, visited_str, graph[current].totalcost])
        df = pd.DataFrame(data, columns=columns)

        if current == goal:
            print(graph[current].totalcost)
            return actionSequence(graph, start, goal), df

        for neighbour, cost in graph[current].actions:
            if neighbour not in visited:
                queue.append(neighbour)
                visited.append(neighbour)
                graph[neighbour].parent = current
                current_cost = graph[current].totalcost
                current_cost += cost
                graph[neighbour].totalcost = current_cost

            elif neighbour in visited:
                if graph[neighbour].totalcost > graph[current].totalcost + cost:
                    graph[neighbour].totalcost = graph[current].totalcost + cost
                    graph[neighbour].parent = current

    return None, df


solution, df = Uniform_cost_search(graph, "S", "G")
print(solution)
print(df)

print(Uniform_cost_search(graph, "S", "G"))
