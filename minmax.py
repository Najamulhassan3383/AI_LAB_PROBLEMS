def minimax(node, depth, maximizingPlayer, evaluate):
    if depth == 0 or node.is_terminal():
        return evaluate(node)
    if maximizingPlayer:
        value = float("-inf")
        for child in node.children():
            value = max(value, minimax(child, depth - 1, False, evaluate))
        return value
    else:
        value = float("inf")
        for child in node.children():
            value = min(value, minimax(child, depth - 1, True, evaluate))
        return value
