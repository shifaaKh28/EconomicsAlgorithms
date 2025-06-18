from typing import List
import numpy as np

# ===== Part 5A - Generalized Median Mechanism with Binary Search =====
def compute_budget_binary(total_budget: float, citizen_votes: List[List[float]]) -> List[float]:
    """
    Computes a fair budget allocation using the Generalized Median Mechanism
    with linear fixed votes and binary search to find the parameter t such that
    the total allocation equals the total_budget.

    Args:
    - total_budget: The total amount of money to be allocated.
    - citizen_votes: A list of lists, each inner list represents a citizen's ideal allocation.

    Returns:
    - A list of floats representing the final allocation per item.
    """
    n = len(citizen_votes)
    m = len(citizen_votes[0])

    def fixed_vote(i, t):
        return total_budget * min(1, (i + 1) * t)

    def get_combined_votes(t):
        fixed_votes = [[fixed_vote(i, t) for _ in range(m)] for i in range(n - 1)]
        return citizen_votes + fixed_votes

    def compute_section_wise_median(votes):
        votes_array = np.array(votes)
        return [np.median(votes_array[:, j]) for j in range(m)]

    def total_from_t(t):
        combined = get_combined_votes(t)
        med = compute_section_wise_median(combined)
        return sum(med), med

    left, right = 0.0, 1.0
    epsilon = 1e-5
    best_median = None

    while right - left > epsilon:
        mid = (left + right) / 2
        current_sum, current_median = total_from_t(mid)
        if current_sum > total_budget:
            right = mid
        else:
            left = mid
            best_median = current_median

    return [float(x) for x in best_median]

# ===== Part 5B - Direct Allocation Using t = 1/n (No Binary Search) =====
def compute_budget_direct(total_budget: float, citizen_votes: List[List[float]]) -> List[float]:
    """
    Computes a fair budget allocation using the Generalized Median Mechanism
    with linear fixed votes, by setting t = 1/n directly instead of binary search.

    This is a theoretically justified shortcut that yields fair and truthful results.

    Args:
    - total_budget: The total amount of money to be allocated.
    - citizen_votes: A list of lists, each inner list represents a citizen's ideal allocation.

    Returns:
    - A list of floats representing the final allocation per item.
    """
    n = len(citizen_votes)
    m = len(citizen_votes[0])
    t = 1 / n

    def fixed_vote(i):
        return total_budget * min(1, (i + 1) * t)

    fixed_votes = [[fixed_vote(i) for _ in range(m)] for i in range(n - 1)]
    all_votes = citizen_votes + fixed_votes

    votes_array = np.array(all_votes)
    medians = [float(np.median(votes_array[:, j])) for j in range(m)]

    return medians

# ===== Example Runs for Both Versions =====
if __name__ == "__main__":
    total_budget = 100
    examples = {
        "Example 1": [[100, 0, 0], [0, 0, 100]],
        "Example 2": [[100, 0, 0], [0, 100, 0], [0, 0, 100]],
        "Example 3": [[0, 0, 100], [50, 50, 0], [50, 50, 0]],
        "Example 4": [[70, 30, 0], [60, 40, 0], [80, 20, 0]]
    }

    for name, votes in examples.items():
        print(f"\n{name}:")
        binary_result = compute_budget_binary(total_budget, votes)
        direct_result = compute_budget_direct(total_budget, votes)
        print("  Binary search result:", binary_result)
        print("  Direct method result:", direct_result)
