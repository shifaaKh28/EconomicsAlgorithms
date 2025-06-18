# Fair Budget Allocation – Assignment 12, Question 5

This project implements **two algorithms** to compute a fair and truthful budget allocation using the **Generalized Median Mechanism (GMM)** with linear fixed votes, based on Lecture 12.

---

## 📌 Problem Overview

Given:
- A total budget `C`
- A set of `n` citizens, each proposing an ideal budget vector over `m` items (summing to `C`)

Goal:
- Aggregate all proposals into a single fair budget allocation
- Satisfy:
  - **Truthfulness**
  - **Group fairness**
  - **(Almost) full budget utilization**

---

## ✅ Implemented Methods

### 1. `compute_budget_binary` (Part A)
- Implements the Generalized Median Mechanism using **binary search** to find the optimal parameter `t*` so that the final budget sum is approximately equal to `C`.
- Time complexity: `O(log(1/ε) * n * m)`
- Accurate and always fully utilizes the budget.

### 2. `compute_budget_direct` (Part B)
- Optimized version that **sets t = 1/n directly** (where `n` is the number of citizens).
- Based on theoretical proof (from Lecture 12) that this choice guarantees:
  - **Truthfulness**
  - **Group fairness**
  - **Approximate total budget**
- Time complexity: `O(n * m)` (faster than binary search)

---

## 🧪 Example Runs

Each example uses `total_budget = 100`.

### 🧾 Inputs Table

| Example | Citizen Votes |
|---------|---------------|
| Example 1 | `[[100, 0, 0], [0, 0, 100]]` |
| Example 2 | `[[100, 0, 0], [0, 100, 0], [0, 0, 100]]` |
| Example 3 | `[[0, 0, 100], [50, 50, 0], [50, 50, 0]]` |
| Example 4 | `[[70, 30, 0], [60, 40, 0], [80, 20, 0]]` |

### 🖼️ Output Example
![image_alt](https://github.com/shifaaKh28/EconomicAlgo-Ass12/blob/main/Screenshot%202025-06-18%20140628.png)

## Output Explanations

- Example 1: Two citizens vote entirely for different items. The fair solution splits the budget equally between the supported items, resulting in [50.0, 0.0, 50.0].

- Example 2: Each citizen supports a distinct item. This results in a perfectly equal division [33.33, 33.33, 33.33] in both methods.

- Example 3: One citizen prefers only item 2, while two others split between items 0 and 1.

The binary search method gives item 2 slightly more weight (20%) due to the strong individual vote.

The direct method favors the majority preference (items 0 and 1), resulting in a higher share for them.

- Example 4: All citizens prefer item 0 the most, with some weight on item 1. Item 2 is ignored.➔ Both methods allocate roughly 2/3 of the budget to item 0 and the rest to item 1.
---

## 🧠 Theoretical Justification for Part B

**Correctness:**
- Using `t = 1/n` ensures the fixed votes are evenly spaced over [0, C], which according to Lecture 12:
  - Preserves truthfulness (median-based mechanism)
  - Ensures group fairness for all size-k subgroups
  - Produces a budget very close to the target `C`

**Efficiency:**
- Avoids binary search entirely.
- Requires only one median computation per item.
- Ideal for large `n` (scalable).

---

## 📂 Files

- `Q5.py`: Python implementation of both algorithms with running examples
- `README.md`: This file, summarizing the solution and theory

---

## ✅ How to Run

```bash
python Q5.py
