class CSP:
    def __init__(self, variables, constraints):
        self.variables = variables
        self.constraints = constraints

    def is_consistent(self, assignment):
        for constraint in self.constraints:
            if not constraint(assignment):
                return False
        return True


def backtracking_search(csp, assignment={}):
    if len(assignment) == len(csp.variables):
        return assignment

    var = select_unassigned_variable(csp, assignment)
    for value in order_domain_values(csp, var, assignment):
        new_assignment = assignment.copy()
        new_assignment[var] = value
        if csp.is_consistent(new_assignment):
            result = backtracking_search(csp, new_assignment)
            if result is not None:
                return result
    return None


def select_unassigned_variable(csp, assignment):
    for var in csp.variables:
        if var not in assignment:
            return var


def order_domain_values(csp, var, assignment):
    return sorted(csp.variables[var])


# Define constraints
def information_aggressiveness_constraint(assignment):
    # Only one class can be chosen from 15-381, 15-681, and 19-601
    selected_classes = [
        assignment.get("Algorithms Requirement"),
        assignment.get("Data Science Requirement"),
    ]
    ai_classes = [assignment.get("Machine Learning Requirement")]
    return len(set(selected_classes)) == len(selected_classes) and len(
        set(ai_classes)
    ) == len(ai_classes)


def basic_arithmetic_constraint(assignment):
    # Either 15-211 or 70-122 can be chosen, not both
    return (
        assignment.get("Algorithms Requirement") != "15-211"
        or assignment.get("Communications Requirement") != "70-122"
    )


def organization_constraint(assignment):
    # Either 21-484 or 70-311 can be chosen, not both
    return (
        assignment.get("Communications Requirement") != "21-484"
        or assignment.get("Communications Requirement") != "70-311"
    )


# Define initial domains for each variable
variables = {
    "Algorithms Requirement": ["15-211", "15-212", "15-381", "15-681", "21-484"],
    "Machine Learning Requirement": ["15-381", "15-681", "80-310"],
    "Communications Requirement": ["21-484", "70-311", "70-122"],
    "Data Science Requirement": ["15-381", "19-601", "15-681"],
}

constraints = [
    information_aggressiveness_constraint,
    basic_arithmetic_constraint,
    organization_constraint,
]

csp = CSP(variables, constraints)
solution = backtracking_search(csp)

if solution:
    print("Solution found:")
    for var, value in solution.items():
        print(f"{var}: {value}")
else:
    print("No solution found.")
