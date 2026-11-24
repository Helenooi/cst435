
import numpy as np
import csv

N = 500

# Generate matrices using a fixed seed
np.random.seed(42)

A = np.random.randint(1, 10, (N, N))
B = np.random.randint(1, 10, (N, N))

# Save Matrix A
np.savetxt("matrix_A_500.csv", A, delimiter=",", fmt="%d")

# Save Matrix B
np.savetxt("matrix_B_500.csv", B, delimiter=",", fmt="%d")

print("Matrices generated successfully!")
print("Matrix A:", A.shape)
print("Matrix B:", B.shape)
