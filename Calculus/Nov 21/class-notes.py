import sympy as sp

## RULE: Deeply explain each step of the calculus problems and notes that follow

# Sectio 5.1 (cont)
#Sigma Notation

# Example 1
# Define the variables
i = sp.symbols('i')
n = sp.symbols('n')

# Define the summation expression
expr = i**2

# Represent the sigma notation
sigma_notation = sp.Sum(expr, (i, 1, n))

# Display the sigma notation
sp.pprint(sigma_notation)