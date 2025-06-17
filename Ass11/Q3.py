#324095702
import cvxpy as cp

def find_decomposition(budget, preferences):
    """
    Determines whether a given participatory budgeting allocation is decomposable (fair),
    and if so, returns a valid decomposition matrix.

    An allocation is decomposable if:
    1. Each agent contributes exactly C/n (where C is the total budget).
    2. The total contribution to each topic equals the given budget for that topic.
    3. Each agent only contributes to topics they support.

    Args:
        budget (list of float): A list of length m representing the budget allocated to each topic.
        preferences (list of set of int): A list of length n where preferences[i] is a set of topic indices supported by agent i.

    Returns:
        list of list of float: A decomposition matrix of shape (n x m), where entry [i][j] is the amount agent i contributes to topic j,
                               or None if no valid decomposition exists.
    """
    n = len(preferences)  # number of agents
    m = len(budget)       # number of topics
    C = sum(budget)       # total budget
    share = C / n         # fair share per agent

    # Create decision variables only for topics supported by each agent
    d = [[None for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in preferences[i]:
            d[i][j] = cp.Variable(nonneg=True)  # only allow non-negative contributions

    constraints = []

    # Constraint 1: For each topic j, the total contributions should equal budget[j]
    for j in range(m):
        contributors = [d[i][j] for i in range(n) if d[i][j] is not None]
        if contributors:
            constraints.append(cp.sum(contributors) == budget[j])
        else:
            # Topic j is not supported by anyone, but has a non-zero budget
            if budget[j] != 0:
                return None

    # Constraint 2: Each agent contributes exactly C/n across all supported topics
    for i in range(n):
        contributions = [d[i][j] for j in preferences[i]]
        if contributions:
            constraints.append(cp.sum(contributions) == share)
        else:
            # Agent supports no topics → must receive zero budget
            if share != 0:
                return None

    # Solve the feasibility problem (no objective function needed)
    prob = cp.Problem(cp.Minimize(0), constraints)
    result = prob.solve()

    if prob.status != cp.OPTIMAL:
        return None  # No valid decomposition found

    # Build and return the decomposition matrix
    decomposition = []
    for i in range(n):
        row = []
        for j in range(m):
            if d[i][j] is not None:
                row.append(round(float(d[i][j].value), 6))
            else:
                row.append(0.0)
        decomposition.append(row)

    return decomposition


# ------------------------
# Example runner

def run_example(budget, preferences, title=""):
    """
    Runs the find_decomposition function with the given inputs and prints the result.

    Args:
        budget (list of float): List of topic budgets.
        preferences (list of set of int): List of agents' preferences over topics.
        title (str): Optional title for the example output.
    """
    print(f"\n--- {title} ---")
    print("Budget:", budget)
    print("Preferences:", preferences)

    result = find_decomposition(budget, preferences)

    if result is None:
        print("❌ The budget is NOT decomposable.")
    else:
        print("✅ Decomposition matrix:")
        for i, row in enumerate(result):
            print(f"Agent {i}: {row}")


# ------------------------
# Main execution block with examples

if __name__ == "__main__":
    # ✅ Example 1: Valid decomposition
    budget1 = [400, 50, 50, 0]
    preferences1 = [
        {0, 1},    # agent 0 supports topics 0 and 1
        {0, 2},    # agent 1 supports topics 0 and 2
        {0, 3},    # agent 2 supports topics 0 and 3
        {1, 2},    # agent 3 supports topics 1 and 2
        {0}        # agent 4 supports topic 0 only
    ]
    run_example(budget1, preferences1, title="Example 1: Valid decomposition")

    # ❌ Example 2: Invalid decomposition (topic unsupported)
    budget2 = [100, 100]
    preferences2 = [
        {0}, {0}, {0}  # no one supports topic 1
    ]
    run_example(budget2, preferences2, title="Example 2: Invalid decomposition (unsupported topic)")
