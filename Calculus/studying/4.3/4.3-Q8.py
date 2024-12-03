### RULE: Every problem must be solved through step-by-step using Calculus while providing the name of the concept used. ###
### RULE: Work the problem through as if you're teaching someone in a Calculus class. ###
### RULE: Create matplotlib graphics for each step to deeply elaborate the steps. ###
### RULE: You MUST come to a definitive answer and stopping point. Think carefully to determine if the problem has been solved. ###
### RULE: If a problem is complex, break it down into manageable parts. ###


import sympy as sp
import numpy as np

# Problem 8
# For the function 
# f(x) = -4x + sin(x)
# find all intervals where the function is increasing.
#  is increasing on 

# (Give your answer as an interval or a list of intervals, e.g., (-infinity,8] or (1,5),(7,10) . Enter none if there are no such intervals.)
# Similarly, find all intervals where the function is decreasing:
#  is decreasing on 

# (Give your answer as an interval or a list of intervals, e.g., (-infinity,8] or (1,5),(7,10) . Enter none if there are no such intervals.)
# Finally, find all critical points in the graph of 
#  (enter 
# values as a comma-separated list, or none if there are no critical points): 

### HINT: Critical points are where the derivative is zero or undefined. ###

# f is increasing on ____:
# f is decreasing on ____:
# Critical Points: ____:

import matplotlib.pyplot as plt

# Define the function and its derivative
x = sp.symbols('x')
f = -4*x + sp.sin(x)
f_prime = sp.diff(f, x)

# Solve for critical points where the derivative is zero
critical_points = sp.solve(f_prime, x)

# Filter out complex solutions
critical_points = [point.evalf() for point in critical_points if point.is_real]

# Determine the intervals of increase and decrease
test_points = [float('-inf')] + [float(point) for point in critical_points] + [float('inf')]
intervals_increasing = []
intervals_decreasing = []
s
for i in range(len(test_points) - 1):
    if test_points[i] == float('-inf'):
        test_value = test_points[i + 1] - 1
    elif test_points[i + 1] == float('inf'):
        test_value = test_points[i] + 1
    else:
        test_value = (test_points[i] + test_points[i + 1]) / 2

    if f_prime.subs(x, test_value).evalf() > 0:
        intervals_increasing.append((test_points[i], test_points[i + 1]))
    else:
        intervals_decreasing.append((test_points[i], test_points[i + 1]))

# Convert intervals to readable format
intervals_increasing = [(a, b) for a, b in intervals_increasing]
intervals_decreasing = [(a, b) for a, b in intervals_decreasing]

# Plot the function
x_vals = np.linspace(-10, 10, 400)
y_vals = [f.subs(x, val) for val in x_vals]

plt.plot(x_vals, y_vals, label='f(x) = -4x + sin(x)')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.legend()
plt.show()

# Output the results
print("f is increasing on:", intervals_increasing)
print("f is decreasing on:", intervals_decreasing)
print("Critical Points:", [float(point) for point in critical_points])