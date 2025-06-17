import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

def is_balanced_matrix(matrix, tol=1e-6):
    """
    Checks if the input matrix is doubly stochastic (i.e., each row and column sums to 1).
    """
    row_sums = matrix.sum(axis=1)
    col_sums = matrix.sum(axis=0)
    return np.allclose(row_sums, 1.0, atol=tol) and np.allclose(col_sums, 1.0, atol=tol)

def plot_bipartite_matrix_with_matching(matrix, matching=None, step_title="", min_weight=None):
    """
    Visualizes the bipartite matrix as a graph.
    Highlights a matching (in red) and optionally displays a title with the step and minimum weight.
    """
    G = nx.Graph()
    num_rows, num_cols = matrix.shape
    left = [f"A{i}" for i in range(num_rows)]
    right = [f"O{j}" for j in range(num_cols)]

    pos = {f"A{i}": (0, -i) for i in range(num_rows)}
    pos.update({f"O{j}": (1, -j) for j in range(num_cols)})

    for i in range(num_rows):
        for j in range(num_cols):
            if matrix[i, j] > 1e-6:
                G.add_edge(f"A{i}", f"O{j}", weight=matrix[i, j])

    edge_colors = []
    edge_widths = []
    for u, v in G.edges():
        i = int(u[1:]) if u.startswith('A') else int(v[1:])
        j = int(v[1:]) if v.startswith('O') else int(u[1:])
        if matching and (i, j) in matching:
            edge_colors.append('red')
            edge_widths.append(3)
        else:
            edge_colors.append('gray')
            edge_widths.append(1)

    labels = nx.get_edge_attributes(G, 'weight')
    labels = {k: f"{v:.2f}" for k, v in labels.items()}

    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(1, 1, 1)

    nx.draw(G, pos, ax=ax, with_labels=True, node_color='lightblue', node_size=2000,
            edge_color=edge_colors, width=edge_widths)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, ax=ax)

    info_text = f"{step_title}"
    if min_weight is not None:
        info_text += f"\nMin Weight to subtract: {min_weight:.2f}"

    fig.text(0.5, 0.96, info_text,
             ha='center', va='top', fontsize=12,
             bbox=dict(boxstyle="round", facecolor="wheat", alpha=0.5))

    plt.subplots_adjust(top=0.88)
    ax.axis('off')
    plt.show()

def find_perfect_matching(matrix):
    """
    Builds a bipartite graph and returns a perfect matching using NetworkX.
    """
    G = nx.Graph()
    num_rows, num_cols = matrix.shape
    left = [f"A{i}" for i in range(num_rows)]
    right = [f"O{j}" for j in range(num_cols)]

    for i in range(num_rows):
        for j in range(num_cols):
            if matrix[i, j] > 1e-6:
                G.add_edge(left[i], right[j], weight=1)

    matching = nx.algorithms.matching.max_weight_matching(G, maxcardinality=True)
    return [(int(a[1:]), int(b[1:])) if a.startswith('A') else (int(b[1:]), int(a[1:])) for a, b in matching]

def birkhoff_decomposition(matrix):
    """
    Performs Birkhoff decomposition on a balanced matrix.
    Returns a list of (matching, weight) pairs.
    """
    if not is_balanced_matrix(matrix):
        raise ValueError("❌ Error: The input matrix is not balanced. Birkhoff decomposition cannot proceed.")

    mat = matrix.copy()
    decompositions = []
    step = 1

    while np.any(mat > 1e-6):
        matching = find_perfect_matching(mat)
        min_weight = min(mat[i, j] for i, j in matching)
        decompositions.append((matching, min_weight))

        plot_bipartite_matrix_with_matching(mat, matching, f"Step {step}: Before Reduction", min_weight)

        for i, j in matching:
            mat[i, j] -= min_weight

        plot_bipartite_matrix_with_matching(mat, None, f"Step {step}: After Reduction")

        step += 1

    return decompositions

def run_example(matrix, title):
    """
    Runs the Birkhoff decomposition for a given matrix, with logging and error handling.
    """
    print(f"\nRunning example: {title}")
    if not is_balanced_matrix(matrix):
        print("⚠️ Matrix is not balanced — expected failure.")
    plot_bipartite_matrix_with_matching(matrix, None, f"{title} - Initial Graph")
    decompositions = birkhoff_decomposition(matrix)
    for i, (match, weight) in enumerate(decompositions, 1):
        print(f"{i}. Matching: {match}, Weight: {weight:.2f}")

# === Run Examples ===
if __name__ == "__main__":
    # ✅ Example 1: From Lecture 9
    matrix_lecture = np.array([
        [0.7, 0.3, 0.0, 0.0],
        [0.0, 0.0, 0.7, 0.3],
        [0.3, 0.0, 0.3, 0.4],
        [0.0, 0.7, 0.0, 0.3]
    ])
    run_example(matrix_lecture, "graph 1 ")

    # ✅ Example 2: 2x2 balanced matrix
    matrix_2x2 = np.array([
        [0.6, 0.4],
        [0.4, 0.6]
    ])
    run_example(matrix_2x2, "graph 2")

    # ✅ Example 3: 3x3 balanced matrix
    matrix_3x3 = np.array([
        [0.3, 0.4, 0.3],
        [0.4, 0.3, 0.3],
        [0.3, 0.3, 0.4]
    ])
    run_example(matrix_3x3, "graph 3")

    # ❌ Example 4: Unbalanced matrix (should raise error)
    matrix_bad = np.array([
        [0.7, 0.3],
        [0.3, 0.3]
    ])
    try:
        run_example(matrix_bad, "graph 4")
    except ValueError as e:
        print(e)
