import cvxpy as cp
import numpy as np

def egalitarian_allocation(value_matrix):
    """
    Solves the egalitarian resource allocation problem.

    Given a matrix of values where value_matrix[i][j] represents the value
    that agent i assigns to resource j, the function computes a division of 
    the resources that maximizes the minimum utility among all agents.

    Parameters:
    -----------
    value_matrix : list of list of floats
        A 2D list where each row corresponds to an agent, and each column
        corresponds to a resource. The values represent the agent's valuation
        of the resources.

    Output:
    -------
    Prints the allocation for each agent, i.e., how much of each resource they receive.
    """

    # Display input matrix
    print("Input value matrix:")
    for i, row in enumerate(value_matrix):
        print(f"Agent #{i+1}: {row}")
    print("\nSolving egalitarian allocation...\n")

    # Convert input to NumPy array
    value_matrix = np.array(value_matrix)
    n_agents, n_resources = value_matrix.shape

    # X[i][j] represents the fraction of resource j given to agent i
    X = cp.Variable((n_agents, n_resources))

    # z represents the minimum utility received by any agent
    z = cp.Variable()

    # Constraints list
    constraints = []

    # Each agent must get at least z utility
    for i in range(n_agents):
        constraints.append(value_matrix[i] @ X[i, :] >= z)

    # Each resource must be fully allocated
    for j in range(n_resources):
        constraints.append(cp.sum(X[:, j]) == 1)

    # No negative allocations
    constraints.append(X >= 0)

    # Optimization goal: maximize the minimum value z
    objective = cp.Maximize(z)
    problem = cp.Problem(objective, constraints)

    # Solve the problem
    problem.solve()

    # Output results
    print("Allocation result:")
    for i in range(n_agents):
        parts = []
        for j in range(n_resources):
            portion = X.value[i, j]
            parts.append(f"{portion:.2f} of resource #{j+1}")
        print(f"Agent #{i+1} gets " + ", ".join(parts) + ".")
    print("\n" + "="*60 + "\n")


# -------------------------------
# Example Runs
# -------------------------------

# Example 1: from the assignment
example_1 = [
    [81, 19, 1],
    [70, 1, 29]
]
egalitarian_allocation(example_1)

# Example 2: three agents, two resources
example_2 = [
    [10, 90],
    [40, 60],
    [80, 20]
]
egalitarian_allocation(example_2)

# Example 3: two agents, four resources
example_3 = [
    [1, 2, 3, 4],
    [4, 3, 2, 1]
]
egalitarian_allocation(example_3)
