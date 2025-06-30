# 324095702
import math
from math import inf

def find_max_Avg_cycle(n, graph):
    """
    Finds the cycle with the maximum average (mean) weight in a directed graph.
    The graph is given as an adjacency matrix. Use -math.inf to indicate no edge.

    Returns:
        Tuple[float, List[int]]: (max_avg_weight, cycle as list of nodes)
    """
    eps = 1e-6

    # Convert adjacency matrix to edge list
    edges = []
    for u in range(n):
        for v in range(n):
            w = graph[u][v]
            if w != -math.inf:
                edges.append((u, v, w))

    # Karp's DP
    dp = [[-inf] * n for _ in range(n + 1)]
    for v in range(n):
        dp[0][v] = 0.0

    incoming = [[] for _ in range(n)]
    for u, v, w in edges:
        incoming[v].append((u, w))

    for k in range(1, n + 1):
        for v in range(n):
            best = -inf
            for u, w in incoming[v]:
                best = max(best, dp[k - 1][u] + w)
            dp[k][v] = best

    # Compute max AVG weight
    max_mean_weight = -inf
    for v in range(n):
        min_avg = inf
        for k in range(n):
            if dp[n][v] > -inf and dp[k][v] > -inf:
                avg = (dp[n][v] - dp[k][v]) / (n - k)
                min_avg = min(min_avg, avg)
        max_mean_weight = max(max_mean_weight, min_avg)

    # Adjusted weights for Bellman-Ford
    adjusted_edges = [(u, v, w - max_mean_weight + eps) for (u, v, w) in edges]
    dist = [0.0] * n
    parent = [-1] * n
    x = -1

    for _ in range(n):
        x = -1
        for u, v, w in adjusted_edges:
            if dist[u] + w > dist[v]:
                dist[v] = dist[u] + w
                parent[v] = u
                x = v
        if x == -1:
            break

    # Recover cycle
    cycle = []
    if x != -1:
        for _ in range(n):
            x = parent[x]
        v = x
        while True:
            cycle.append(v)
            v = parent[v]
            if v == x:
                break
        cycle.reverse()
        cycle.append(cycle[0])

    if max_mean_weight < 0:
        return 0, []
    return max_mean_weight, cycle

def normalize_cycle(cycle):
    if not cycle:
        return cycle
    min_index = cycle.index(min(cycle[:-1]))
    return cycle[min_index:-1] + cycle[:min_index] + [cycle[min_index]]

def run_example(name, graph):
    n = len(graph)
    max_avg, cycle = find_max_Avg_cycle(n, graph)
    cycle = normalize_cycle(cycle)
    print(f"\n=== Example: {name} ===")
    if cycle:
        print("Cycle with the max avg is:")
        print(" ", " → ".join(map(str, cycle)))
        print(f"Max average: {max_avg:.3f}")
    else:
        print("No cycle found.")


# test cases: 
if __name__ == "__main__":
    # === Example 1: Simple Triangle ===
    # 0 → 1 (2), 1 → 2 (5), 2 → 0 (7)
    graph1 = [
        [-inf, 10,    -inf],
        [-inf, -inf, 2   ],
        [6,    -inf, -inf]
    ]

    # === Example 2: 5 nodes ===
    # 0 → 1 (2), 0 → 4 (4)
    # 1 → 2 (5), 1 → 3 (1)
    # 2 → 0 (7), 2 → 3 (1)
    # 3 → 1 (1)
    # 4 → 2 (3)
    graph2 = [
        [ -math.inf, 2,          -math.inf, -math.inf, 4         ],
        [ -math.inf, -math.inf,  5,         1,         -math.inf ],
        [ 7,         -math.inf,  -math.inf, 1,         -math.inf ],
        [ -math.inf, 1,          -math.inf, -math.inf, -math.inf ],
        [ -math.inf, -math.inf,  3,         -math.inf, -math.inf ]
    ]


    # === Example 3: 4 nodes ===
    graph3 = [
    [-math.inf, 1,         -math.inf, 8],   # 0 → 1, 0 → 3
    [-math.inf, -math.inf, 3,         -math.inf],  # 1 → 2
    [10,        -math.inf, -math.inf, -math.inf],  # 2 → 0
    [-math.inf, 0,         2,         -math.inf]   # 3 → 1, 3 → 2
]

    run_example("Circular Graph (v1→v2→v3→v1 + v4)", graph3)

      # === Example 5: 4-node square with diagonals (numbered nodes) ===
    # Edges:
    # 0 → 1 (9), 1 → 3 (7), 3 → 1 (11)
    # 3 → 2 (6), 2 → 0 (10), 2 → 3 (5), 3 → 0 (14)
    graph4 = [
        [-math.inf, 9,         -math.inf, -math.inf],
        [-math.inf, -math.inf, -math.inf, 7],
        [10,        -math.inf, -math.inf, 5],
        [14,        11,        6,         -math.inf]
    ]

    run_example("Triangle Graph", graph1)
    run_example("Multi-cycle Graph", graph2)
    run_example("Circular Graph (v1→v2→v3→v1 + v4)", graph3)
    run_example("4-Node Graph with Diagonals", graph4)
  
