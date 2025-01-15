### RULE: Every problem must be solved through step-by-step using Calculus while providing the name of the concept used. ###
### RULE: Work the problem through as if you're teaching someone in a Calculus class. ###
### RULE: Create matplotlib graphics for each step to deeply elaborate the steps. ###
### RULE: You MUST come to a definitive answer and stopping point. Think carefully to determine if the problem has been solved. ###
### RULE: If a problem is complex, break it down into manageable parts. ###


# f(x) = ((x^4)/4) - 3x^3 + 3

# determine the intervals on which the function is concave up or concave down.
# f is concave up on (-inf, 0) and (6, inf)
# f is concave down on (0, 6)
# The inflection points are at x = 0 and x = 6.

# Step 1: Find the first derivative of f(x).
# The first derivative of f(x) is f'(x) = x^3 - 9x^2
# Step 2: Find the second derivative of f(x).
# The second derivative of f(x) is f''(x) = 3x^2 - 18x
# Step 3: Find critical numbers and relative extrema.
# To find where the function is concave up, we need to find where the second derivative is positive.
# We need to solve the inequality 3x^2 - 18x > 0
# Factor out a 3x to get 3x(x - 6) > 0
# Deeply explain
# The critical points are x = 0 and x = 6
# We can use a number line to test the intervals.

# Help me understand with plotly and ipywidgets
import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, diff, solve

x = symbols('x')
f = (x**4)/4 - 3*x**3 + 3
f_prime = diff(f, x)
f_double_prime = diff(f_prime, x)
critical_points = solve(f_double_prime, x)
critical_points

x_vals = np.linspace(-10, 10, 400)
y_vals = [f.subs(x, i) for i in x_vals]
y_prime_vals = [f_prime.subs(x, i) for i in x_vals]
y_double_prime_vals = [f_double_prime.subs(x, i) for i in x_vals]

plt.figure(figsize=(12, 6))
plt.plot(x_vals, y_vals, label='f(x)')
plt.plot(x_vals, y_prime_vals, label="f'(x)")
plt.plot(x_vals, y_double_prime_vals, label="f''(x)")
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.scatter(critical_points, [f.subs(x, i) for i in critical_points], color='red', zorder=5)
plt.legend()
plt.show()

# The graph of f(x) shows the function is concave up on the intervals (-∞, 0) and (6, ∞).