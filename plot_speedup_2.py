
import matplotlib.pyplot as plt

# Matrix sizes
matrix_sizes = [50, 100, 200, 500]

# Speedup results
speedup_2 = [0.882948, 0.937334, 1.157975, 0.994695]
speedup_4 = [0.796539, 0.965996, 1.145598, 1.008569]
speedup_6 = [0.670709, 0.914109, 0.985545, 0.971429]

# Plot speedup
plt.figure(figsize=(9, 5))

plt.plot(matrix_sizes, speedup_2, marker='o', label='2 Threads')
plt.plot(matrix_sizes, speedup_4, marker='o', label='4 Threads')
plt.plot(matrix_sizes, speedup_6, marker='o', label='6 Threads')

# Reference line
plt.axhline(y=1, linestyle='--')

plt.title('Plot 2: Matrix Size vs Speedup')
plt.xlabel('Matrix Size')
plt.ylabel('Speedup (x)')

plt.xticks(matrix_sizes)
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.savefig('plot2_speedup.png', dpi=300)
plt.show()
