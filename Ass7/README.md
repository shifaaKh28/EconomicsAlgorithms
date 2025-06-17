# Maximum Mean Cycle in Directed Graph

This project implements an algorithm to find the **cycle with the maximum average (mean) weight** in a **directed graph**.

---

##  Problem Definition

Given a **directed graph** with real weights , find a cycle (if one exists) such that the **average weight per edge** in the cycle is **maximized**.

The input is an **adjacency matrix** `graph`, where `-inf` represents absence of an edge.

---

##  Algorithm Used: Karp's Algorithm

We use the **Karp algorithm**, which is a dynamic programming-based method to compute the **maximum mean cycle** in a graph.

### Steps:
1. Build a table `dp[k][v]` representing the maximum weight of any path of length `k` ending at vertex `v`.
2. For each vertex `v`, compute:
   \[
   \min_{k < n} \frac{dp[n][v] - dp[k][v]}{n - k}
   \]
   and take the maximum across all vertices. This gives the **maximum mean weight** `μ*`.
3. Shift all edge weights by `w' = w - μ* + ε`, and run **Bellman-Ford** to detect a positive-weight cycle (indicating a mean > μ*).
4. Reconstruct the actual cycle.

---

## Time Complexity

- `dp` table computation: `O(n * m)`
- Mean weight calculations: `O(n^2)`
- Bellman-Ford cycle detection: `O(n * m)`
- Cycle recovery: `O(n)`

### 🔹 Total runtime: **O(n * m)** = O(n^3)⇒ **Polynomial time**

