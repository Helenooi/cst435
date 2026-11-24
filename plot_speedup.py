
import pandas as pd
import matplotlib.pyplot as plt

# =====================================
# 1. READ EXCEL FILE
# =====================================

file_path = "CST435_Assignment1.xlsx"

df = pd.read_excel(
    file_path,
    sheet_name="Analysis",
    header=1
)

# =====================================
# 2. FILTER THREAD CONFIGURATIONS
# =====================================

threads = [2, 4, 6]

# =====================================
# 3. PLOT MATRIX SIZE VS SPEEDUP
# =====================================

plt.figure(figsize=(9, 5))

for thread in threads:

    # Select data for the current thread
    data = df[df["Phthread"] == thread].sort_values("Matrix Size")

    plt.plot(
        data["Matrix Size"],
        data["Speedup"],
        marker="o",
        label=f"{thread} Threads"
    )

# Chart title and labels
plt.title("Plot 2: Matrix Size vs Speedup")
plt.xlabel("Matrix Size")
plt.ylabel("Speedup (x)")

plt.xticks([50, 100, 200, 500])

plt.grid(True)
plt.legend()

plt.tight_layout()

# Save chart
plt.savefig("plot2_speedup.png", dpi=300)

# Display chart
plt.show()
