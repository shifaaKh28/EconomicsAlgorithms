

# Decomposable Participatory Budgeting Checker 

This Python script provides a solution to the problem of determining whether a given continuous participatory budget is **decomposable** (i.e., fair according to certain mathematical criteria), and if so, returns a valid decomposition of that budget among agents.

---

## 📘 Problem Overview

In **participatory budgeting**, a set of agents vote on a set of topics (projects). A total budget is given and already allocated to each topic. We want to verify whether this allocation is **decomposable**, meaning it can be explained by fair and rational contributions from the agents.

### 🔍 What Is a Decomposable Budget?

A budget allocation is *decomposable* if:

1. Each agent contributes exactly `C/n` where:
   - `C` is the total budget
   - `n` is the number of agents

2. Each agent only contributes to topics they support.

3. The sum of contributions to each topic equals the budget assigned to that topic.

---

## ⚙️ Function Description

```python
def find_decomposition(budget: list[float], preferences: list[set[int]]) -> Optional[list[list[float]]]
````

### Arguments:

* `budget`: A list of floats, where `budget[j]` is the amount allocated to topic `j`.
* `preferences`: A list of sets, where `preferences[i]` contains the indices of topics supported by agent `i`.

### Returns:

* If a valid decomposition exists: returns an `n x m` matrix where `result[i][j]` is the amount agent `i` contributes to topic `j`.
* If the budget is not decomposable: returns `None`.

The function uses [CVXPY](https://www.cvxpy.org/) to formulate the problem as a linear program and solves it as a **feasibility problem** (i.e., no optimization objective, just checking if constraints can be satisfied).

---

## 🧪 Example Usage

The script includes a runner that prints results for two different test cases:

### ✅ Example 1: Valid Decomposition

```python
budget = [400, 50, 50, 0]
preferences = [
    {0, 1}, {0, 2}, {0, 3}, {1, 2}, {0}
]
```

#### Explanation:

* Total budget = 500, number of agents = 5 ⇒ each agent must contribute exactly 100.
* All topics that received a budget are supported by at least one agent.
* The decomposition matrix returned splits the budget in a way that satisfies all fairness rules.

#### Output:

```
✅ Decomposition matrix:
Agent 0: [100.0, 0.0, 0.0, 0.0]
Agent 1: [100.0, 0.0, 0.0, 0.0]
Agent 2: [100.0, 0.0, 0.0, 0.0]
Agent 3: [0.0, 50.0, 50.0, 0.0]
Agent 4: [100.0, 0.0, 0.0, 0.0]
```

---

### ❌ Example 2: Invalid Decomposition (Unsupported Topic)

```python
budget = [100, 100]
preferences = [
    {0}, {0}, {0}
]
```

#### Explanation:

* Topic 1 received a budget of 100, but **no agent supports it**.
* There is no way to assign that money fairly without violating the support constraint.
* Hence, the budget is **not decomposable**.

#### Output:

```
❌ The budget is NOT decomposable.
```

---

## 📦 Dependencies

To run this script, make sure to install [CVXPY](https://www.cvxpy.org/):

```bash
pip install cvxpy
```
