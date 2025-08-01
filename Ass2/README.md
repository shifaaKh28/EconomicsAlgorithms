
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


