import numpy as np
import matplotlib.pyplot as plt

# Define the function
def f(x):
    return (x**2) / 12

# Create data for smooth curve
x = np.linspace(4, 8, 200)
y = f(x)

# Create subintervals
n = 8  # number of subintervals
x_points = np.linspace(4, 8, n+1)
dx = 0.5  # width of each subinterval

# Create figure and axis
fig, ax = plt.subplots(figsize=(12, 6))

# Plot the function
ax.plot(x, y, 'b-', label='f(x) = x²/12')

# Plot left endpoint rectangles
for i in range(n):
    x_left = x_points[i]
    y_left = f(x_left)
    ax.add_patch(plt.Rectangle((x_left, 0), dx, y_left, 
                              facecolor='green', alpha=0.3))

# Plot right endpoint rectangles
for i in range(n):
    x_right = x_points[i+1]
    y_right = f(x_right)
    ax.add_patch(plt.Rectangle((x_points[i], 0), dx, y_right, 
                              facecolor='red', alpha=0.3))

# Add rectangles to legend
ax.add_patch(plt.Rectangle((0,0), 1, 1, facecolor='green', alpha=0.3, 
             label=f'Left sum ≈ {11.45825:.4f}'))
ax.add_patch(plt.Rectangle((0,0), 1, 1, facecolor='red', alpha=0.3, 
             label=f'Right sum ≈ {13.45825:.4f}'))

# Customize the plot
ax.grid(True, linestyle='--', alpha=0.7)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Left and Right Riemann Sums for f(x) = x²/12 on [4,8]')
ax.legend()

# Set axis limits
ax.set_xlim(3.5, 8.5)
ax.set_ylim(0, 6)

plt.show()
