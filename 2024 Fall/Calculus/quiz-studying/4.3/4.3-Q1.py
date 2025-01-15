### RULE: Every problem must be solved through step-by-step using Calculus while providing the name of the concept used. ###
### RULE: Work the problem through as if you're teaching someone in a Calculus class. ###
### RULE: Create matplotlib graphics for each step to deeply elaborate the steps. ###
### RULE: You MUST come to a definitive answer and stopping point. Think carefully to determine if the problem has been solved. ###
### RULE: If a problem is complex, break it down into manageable parts. ###

# For what values of x is the graph of y = xe^(-4x) concave down?
# Give answer in interval notation.

# Concept:
## To find the concavity of a function, we need to find the second derivative of the function and determine where it is negative.

# Given function:
## f(x) = xe^(-4x)

# First derivative:
## f'(x) = e^(-4x) - 4xe^(-4x)

# Second derivative:
## f''(x) = 16xe^(-4x) - 8e^(-4x)

# To find the concavity of the function, we need to find where the second derivative is negative.
## 16xe^(-4x) - 8e^(-4x) < 0
## 8e^(-4x)(2x - 1) < 0
## e^(-4x)(2x - 1) < 0 (What happens to the 8?) answer: 8 is positive, so it doesn't affect the sign of the inequality.
## e^(-4x) > 0 and 2x - 1 < 0 (explain) answer: e^(-4x) is always positive, so we only need to consider 2x - 1 < 0.

# Solve 2x - 1 < 0
## 2x < 1
## x < 1/2

# The graph of y = xe^(-4x) is concave down for x < 1/2.

# Answer:
## (-∞, 1/2)

# Let's visualize the function and the concavity of the function.
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1, 1, 400)
y = x * np.exp(-4 * x)
y_prime = np.exp(-4 * x) - 4 * x * np.exp(-4 * x)
y_double_prime = 16 * x * np.exp(-4 * x) - 8 * np.exp(-4 * x)

plt.figure(figsize=(10, 6))
plt.plot(x, y, label='y = xe^(-4x)')
plt.plot(x, y_prime, label="y' = e^(-4x) - 4xe^(-4x)")
plt.plot(x, y_double_prime, label="y'' = 16xe^(-4x) - 8e^(-4x)")
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.axvline(0.5, color='red', linewidth=0.5, linestyle='--', label='x = 1/2')
plt.legend()
plt.title('Function and its Derivatives')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()