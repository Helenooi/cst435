
import numpy as np
import time


def sequential_matrix_multiplication(A, B):
    """
    Multiply two matrices sequentially.
    """

    rows_A = len(A)
    cols_A = len(A[0])
    cols_B = len(B[0])

    # Create an empty result matrix
    C = [[0 for j in range(cols_B)] for i in range(rows_A)]

    # Sequential matrix multiplication
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                C[i][j] += A[i][k] * B[k][j]

    return C


if __name__ == "__main__":

    # Read matrices from CSV files
    A = np.loadtxt("matrix_A_500.csv", delimiter=",", dtype=int).tolist()
    B = np.loadtxt("matrix_B_500.csv", delimiter=",", dtype=int).tolist()

    # Check whether matrix dimensions are compatible
    if len(A[0]) != len(B):
        raise ValueError("Matrix dimensions are not compatible!")

    # Measure execution time
    start_time = time.perf_counter()

    result = sequential_matrix_multiplication(A, B)

    end_time = time.perf_counter()

    execution_time = end_time - start_time

    # Display results
    print("===== Sequential Matrix Multiplication =====")

    print("\nMatrix A dimensions:", len(A), "x", len(A[0]))
    print("Matrix B dimensions:", len(B), "x", len(B[0]))

    print("\nMatrix A:")
    print(A)

    print("\nMatrix B:")
    print(B)

    print("\nResult Matrix:")
    print(result)

    print("\nResult dimensions:", len(result), "x", len(result[0]))

    print("\nExecution Time:", execution_time, "seconds")
