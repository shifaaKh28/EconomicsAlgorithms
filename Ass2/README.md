
# Egalitarian Allocation using CVXPY

This project solves the **egalitarian allocation problem** using convex optimization (via `cvxpy` in Python).  
The goal is to divide a set of resources between agents in a way that is **as fair as possible**, by maximizing the **minimum satisfaction** (utility) of any agent.

---

## 📚 What is Egalitarian Allocation?

In economics and fair division theory, **egalitarian allocation** refers to a strategy that prioritizes the **worst-off agent** by:

> Maximizing the utility of the agent who receives the least.

This ensures that **no one is left far behind**, even if the total utility is not maximized.

---

## 📐 Formal Problem Statement

Given:
- `n` agents
- `m` resources
- A matrix `V` of size `n × m` where `V[i][j]` is the value agent `i` assigns to resource `j`.

Let `X[i][j]` be the portion of resource `j` allocated to agent `i`.

We want to find `X` that:

1. Maximizes `z = min_i (utility_i)`
2. Subject to:
   - Each resource is fully divided:  
     \[ \sum_i X[i][j] = 1 \quad \forall j \]
   - Each agent receives at least `z` value:  
     \[ \sum_j V[i][j] \cdot X[i][j] \geq z \quad \forall i \]
   - No agent receives a negative amount:  
     \[ X[i][j] \geq 0 \]

---

## ⚙️ Installation

Make sure you have Python installed (version 3.7+ recommended).  
Install the required packages:

```bash
pip install cvxpy numpy
```

---

## 🚀 How to Run

Simply run the `egalitarian_allocation.py` script.  
It includes **three predefined examples**.

```bash
python egalitarian_allocation.py
```

---

## 📊 Example Runs and Explanation
![image_alt](https://github.com/shifaaKh28/EconomicsAlgorithms/blob/main/Ass2/Screenshot%202025-06-22%20182002.png)

---

### ✅ Example 1: Based on the assignment

**Input matrix:**

```python
[
    [81, 19, 1],
    [70, 1, 29]
]
```

**Output:**

```
Agent #1 gets 0.47 of resource #1, 1.00 of resource #2, and 0.00 of resource #3.
Agent #2 gets 0.53 of resource #1, 0.00 of resource #2, and 1.00 of resource #3.
```

**Explanation:**  
The allocation ensures that both agents get utility as high as possible. Agent 1 gets full access to resource #2 and almost half of #1. Agent 2 compensates by receiving all of #3 and the rest of #1.

---

### ✅ Example 2: Three agents, two resources

**Input matrix:**

```python
[
    [10, 90],
    [40, 60],
    [80, 20]
]
```

**Output:**

```
Agent #1 gets 0.00 of resource #1, 0.41 of resource #2.
Agent #2 gets 0.00 of resource #1, 0.59 of resource #2.
Agent #3 gets 1.00 of resource #1, 0.00 of resource #2.
```

**Explanation:**  
- Agent 3 values resource #1 the most and gets it entirely.  
- Agents 1 and 2 split resource #2 based on their preferences.  
- No agent is left out — fairness is maintained by maximizing the **minimum utility**.

---

### ✅ Example 3: Two agents, four resources

**Input matrix:**

```python
[
    [1, 2, 3, 4],
    [4, 3, 2, 1]
]
```

**Output:**

```
Agent #1 gets 0.00 of resource #1, 0.00 of resource #2, 0.50 of resource #3, 1.00 of resource #4.
Agent #2 gets 1.00 of resource #1, 1.00 of resource #2, 0.50 of resource #3, 0.00 of resource #4.
```

**Explanation:**  
- Preferences are symmetric but opposite.  
- The algorithm splits resource #3 evenly.  
- Each agent receives the resources they value most, without conflict.  
- The minimum utility is maximized while keeping the total allocation fair.

---


