class Node:
    def __init__(self, state, parent, actions, totalcost):
        self.state = state
        self.parent = parent
        self.actions = actions
        self.totalcost = totalcost


# a => nothing
# b => a
# c => a
# d => b, c
# e => h,r
# f => g,c
# g => nothing
# h => p,q
# p => q
# r => f
# s => p,e,d


graph = {
    "A": Node("A", None, [], None),
    "B": Node("B", None, ["A"], None),
    "C": Node("C", None, ["A"], None),
    "D": Node("D", None, ["B", "C"], None),
    "E": Node("E", None, ["H", "R"], None),
    "F": Node("F", None, ["G", "C"], None),
    "G": Node("G", None, [], None),
    "H": Node("H", None, ["P", "Q"], None),
    "P": Node("P", None, ["Q"], None),
    "R": Node("R", None, ["F"], None),
    "S": Node("S", None, ["P", "E", "D"], None),
}
