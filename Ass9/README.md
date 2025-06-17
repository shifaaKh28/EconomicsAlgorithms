# Birkhoff Decomposition Visualizer 🧮🎨

This project implements and visualizes the **Birkhoff–von Neumann decomposition** algorithm, which expresses a doubly stochastic matrix as a convex combination of permutation matrices.

---

## 🔍 What is Birkhoff Decomposition?

Given a matrix where:
- Each row and column sums to 1
- All entries are non-negative

It can be decomposed into a weighted sum of **permutation matrices** (perfect matchings).
## 🖼️ Sample Output Plots


![](img/Screenshot%202025-05-22%20224158.png)

![](img/Screenshot%202025-05-22%20224205.png)

![](img/Screenshot%202025-05-22%20224213.png)



![](img/Screenshot%202025-05-22%20224221.png)

![](img/Screenshot%202025-05-22%20224229.png)

![](img/Screenshot%202025-05-22%20224236.png)

![](img/Screenshot%202025-05-22%20224242.png)


### 🔸 Final Matrix

![Final Matrix](img/Screenshot%202025-05-22%20224333.png)

---

## 📦 Features

- ✅ Detects whether a matrix is balanced (doubly stochastic)
- ✅ Performs step-by-step Birkhoff decomposition
- ✅ Visualizes the bipartite matching and matrix at each step
- ✅ Highlights current matching and minimum weight used
- ❌ Fails gracefully for unbalanced matrices

---

## 🚀 How to Run

### Requirements

Install the necessary Python packages:

```bash
pip install numpy matplotlib networkx
