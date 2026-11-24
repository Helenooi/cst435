import numpy as np
import time
import threading
import sys


def multiply_rows(A, B, C, start_row, end_row):
    """
    Multiply assigned rows of two matrices.
    """

    cols_A = len(A[0])
    cols_B = len(B[0])

    # Same matrix multiplication algorithm
    for i in range(start_row, end_row):
        for j in range(cols_B):
            for k in range(cols_A):
                C[i][j] += A[i][k] * B[k][j]


def multithread_matrix_multiplication(A, B, num_threads):
    """
    Multiply two matrices using multithreading.
    """

    rows_A = len(A)
    cols_B = len(B[0])

    # Create an empty result matrix
    C = [[0 for j in range(cols_B)] for i in range(rows_A)]

    num_threads = min(num_threads, rows_A)

    threads = []

    # Parallel matrix multiplication
    for t in range(num_threads):

        start_row = t * rows_A // num_threads
        end_row = (t + 1) * rows_A // num_threads

        thread = threading.Thread(
            target=multiply_rows,
            args=(A, B, C, start_row, end_row)
        )

        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    return C


if __name__ == "__main__":

    num_threads = 4

    if len(sys.argv) > 1:
        num_threads = int(sys.argv[1])

    if num_threads < 1:
        raise ValueError("Number of threads must be at least 1!")

    # Read matrices from CSV files
    A = np.loadtxt("matrix_A_500.csv", delimiter=",", dtype=int).tolist()
    B = np.loadtxt("matrix_B_500.csv", delimiter=",", dtype=int).tolist()

    # Check whether matrix dimensions are compatible
    if len(A[0]) != len(B):
        raise ValueError("Matrix dimensions are not compatible!")

    # Measure execution time
    start_time = time.perf_counter()

    result = multithread_matrix_multiplication(A, B, num_threads)

    end_time = time.perf_counter()

    execution_time = end_time - start_time

    # Display results
    print("===== Multithreading Matrix Multiplication =====")

    print("\nMatrix A dimensions:", len(A), "x", len(A[0]))
    print("Matrix B dimensions:", len(B), "x", len(B[0]))

    print("\nNumber of Threads:", min(num_threads, len(A)))

    print("\nMatrix A:")
    print(A)

    print("\nMatrix B:")
    print(B)

    print("\nResult Matrix:")
    print(result)

    print("\nResult dimensions:", len(result), "x", len(result[0]))

    print("\nExecution Time:", execution_time, "seconds")