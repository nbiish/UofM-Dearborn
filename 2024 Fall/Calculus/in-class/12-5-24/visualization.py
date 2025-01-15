import numpy as np
import matplotlib.pyplot as plt

# Create time points for interval [0, 7]
t = np.linspace(0, 7, 1000)

# Define velocity function v(t) = 2t-10
v = 2*t - 10

# Custom numerical integration function using trapezoidal rule
def integrate(y, x):
    dx = x[1] - x[0]
    integral = np.zeros(len(x))
    for i in range(1, len(x)):
        integral[i] = integral[i-1] + (y[i] + y[i-1])/2 * dx
    return integral

# Calculate position by integrating velocity
s = integrate(v, t)

# Calculate total distance using absolute velocity
total_distance = integrate(np.abs(v), t)

# Create subplots
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 12))

# Plot velocity
ax1.plot(t, v, 'b-', label='v(t) = 2t-10')
ax1.axhline(y=0, color='k', linestyle='-', alpha=0.3)
ax1.axvline(x=5, color='r', linestyle='--', label='t=5 (v=0)')
ax1.set_title('Velocity vs Time')
ax1.set_xlabel('Time (t)')
ax1.set_ylabel('Velocity (m/s)')
ax1.grid(True)
ax1.legend()

# Plot position (displacement)
ax2.plot(t, s, 'g-', label='Position')
ax2.axhline(y=0, color='k', linestyle='-', alpha=0.3)
ax2.plot([0, 7], [0, -21], 'r--', label='Net displacement (-21m)')
ax2.set_title('Position vs Time')
ax2.set_xlabel('Time (t)')
ax2.set_ylabel('Position (m)')
ax2.grid(True)
ax2.legend()

# Plot total distance
ax3.plot(t, total_distance, 'r-', label='Total Distance')
ax3.axhline(y=29, color='g', linestyle='--', label='Total distance (29m)')
ax3.set_title('Total Distance vs Time')
ax3.set_xlabel('Time (t)')
ax3.set_ylabel('Distance (m)')
ax3.grid(True)
ax3.legend()

plt.tight_layout()
plt.show()