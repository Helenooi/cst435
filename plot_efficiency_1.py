
import matplotlib.pyplot as plt

# Matrix sizes
matrix_sizes = [50, 100, 200, 500]

# Parallel efficiency results (%)
efficiency_2 = [44.14741, 46.86671, 57.89874, 49.73476]
efficiency_4 = [19.91347, 24.14990, 28.63994, 25.21422]
efficiency_6 = [11.17848, 15.23515, 16.42575, 16.19048]

# Plot efficiency
plt.figure(figsize=(9, 5))

plt.plot(matrix_sizes, efficiency_2, marker='o', label='2 Threads')
plt.plot(matrix_sizes, efficiency_4, marker='o', label='4 Threads')
plt.plot(matrix_sizes, efficiency_6, marker='o', label='6 Threads')

plt.title('Plot 3: Matrix Size vs Parallel Efficiency')
plt.xlabel('Matrix Size')
plt.ylabel('Parallel Efficiency (%)')

plt.xticks(matrix_sizes)
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.savefig('plot3_efficiency.png', dpi=300)
plt.show()
