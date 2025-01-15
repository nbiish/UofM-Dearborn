import numpy as np
import matplotlib.pyplot as plt

def total_fence_length(L):
    W = 3_000_000 / L
    return 3*L + 2*W

# Generate points for plotting
L = np.linspace(500, 2500, 1000)
fence_length = total_fence_length(L)

# Calculate the minimum point
L_min = 1000 * np.sqrt(2)  # ≈ 1414.21
min_fence = total_fence_length(L_min)

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(L, fence_length, 'b-', label='Total Fence Length')
plt.plot(L_min, min_fence, 'ro', label='Minimum Point')

# Add annotations
plt.annotate(f'Minimum: ({L_min:.0f}, {min_fence:.0f})',
            (L_min, min_fence),
            xytext=(L_min+200, min_fence+500),
            arrowprops=dict(facecolor='black', shrink=0.05))

plt.title('Optimization of Rectangular Field Fence Length')
plt.xlabel('Length (feet)')
plt.ylabel('Total Fence Length (feet)')
plt.grid(True)
plt.legend()

# Set reasonable axis limits
plt.ylim(8000, 12000)

plt.show()