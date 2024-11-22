## RULE: Deeply explain each step of the calculus problems and notes that follow
## RULE: Keep notation as fractions as much as possible
# Sectio 5.1 (cont)
#Sigma Notation

# Example 1

# TO FILL LATER


# Notes
# So area is limit of Riemann sum as n approaches infinity

# Section 5.2
# DEFINITION: The definite integral of f from a to b is the limit of the Riemann sum as the maximum width of the subintervals approaches zero

# Terminilogy:
# _____ called an intergral sign (looks like a stretched out S)
# a and b are called the limits of integration
# (a is the lower limit and b is the upper limit)
# f(x) is called the integrand
# dx is the differential of x

# If f(x) greater than or equal to 0 on [a,b], then the definite integral of f from a to b is the area under the curve y=f(x) from x=a to x=b

# If f(x) is positive on [a,b] and negative on [a,b], ...
# ...insterfral of f from a to b is the sum of the areas above ...
# ... the x-axis minus the areas below the x-axis called...
# ...the net area
# Where A__1 is the area above the x-axis and below the curve...
#... and A__2 is the area below the x-axis and above the curve.

# Example 2
# Find the definite integral of f(x) = 2 - x from -1 to 3
# Graph the intergral f(x) = 2 - x, y = 2 - x from -1 to 3
# Area is 1/2 * base * height
# A__1 = 1/2 * 3 * 3 = 4.5
# A__2 = 1/2 * 1 * 1 = 0.5
# Net area = 4.5 - 0.5 = 4

# Midpoint Rule
# Definite integral of f from a to b is approximately equal to f(x_bar_1) * delta_x + f(x_bar_2) * delta_x + ... + f(x_bar_n) * delta_x
# Where n is number of subintervals (rectangles/intervals)
# x_bar_i is the midpoint of the i-th subinterval
# delta_x = (b - a) / n

# Example 3
# Use Midpoint Rule with n=4 to estimate ...
#... the definite integral of f(x) = (x/sqrt(1 + 2x)) * dx from 1 to 3 ...
#... round to 3 decimal places
# delta_x = b - a / n = 3 - 1 / 4 = 0.5
# x_bar_1 = 1 + 0.25 = 1.25
# x_bar_2 = 1.75
# x_bar_3 = 2.25

# Subintervals | Midpoint
# [1, (3/2)] | (1+3/2)/2 = 5/4 = x_bar_1
# [(3/2), 2] | (3/2 + 2)/2 = 7/4 = x_bar_2
# [2, (5/2)] | (2 + 5/2)/2 = 9/4 = x_bar_3
# [(5/2), 3] | (5/2 + 3)/2 = 11/4 = x_bar_4

# defintie integral of f(x) = (x/sqrt(1 + 2x)) * dx from 1 to 3 ...
# ... is approximately equal to ...
# ... f(x_bar_1) * delta_x + f(x_bar_2) * delta_x + f(x_bar_3) * delta_x + f(x_bar_4) * delta_x ...
# ... ~= f(5/4) * 0.5 + f(7/4) * 0.5 + f(9/4) * 0.5 + f(11/4) * 0.5 ...
# ... ~= (5/4)/sqrt(1 + 2(5/4)) * 0.5 + (7/4)/sqrt(1 + 2(7/4)) * 0.5 ...
# ... ~= 1.766

# FACTS:
# the definite integral of f(x)*dx from a to b is equal to the definite integral of -f(x)*dx from b to a
# So when reverse limits of integration, you get the negative of the original integral
# The definite integral of f(x) from a to a is 0    (area under the curve from a to a is 0)

# Properties of Definite Integrals
# 1. The definite integral of a constant times the derivative of f(x) from a to b is equal to the constant times b - a when c is a constant
# ---WHY?---
# Integral is f(x) = c
# y = c (horizontal line)
# Area = c * (b - a)
# QED

# TO FILL LATER

# 3. The definite integral of c * f(x) * dx from a to b is equal to c times the definite integral of f(x) * dx from a to b
# i.e. a constant multiple can be factored out of the integral sign

# 2 & 4. The definite integral of f(x) + or - g(x) * dx from a to b is equal to the definite integral of f(x) * dx from a to b + or - the definite integral of g(x) * dx from a to b
# i.e. the integral of a sum or difference of functions is the sum or difference of the integrals of the functions

# 5. If a < b < c, then the definite integral of f(x) * dx from a to c is equal to the definite integral of f(x) * dx from a to b + the definite integral of f(x) * dx from b to c
# ---WHY?---
# Area from a to c is the sum of the area from a to b and b to c

# Theorem 3:
# if f(x) is continuous or has a finite of discontinuities (none of which are infinite discontinuities) then f is integrable on [a,b]
# i.e. the definite integral of f(x) * dx from a to b exists

# Example 4
# If f(x) = piecewise function defined as follows:
# ... -4 for x < 2
# ... x for 2 <= x < 5
# ... -3 for x >= 5
# Find the definite integral of f(x) * dx from 0 to 6
# Use property 5 to split the integral 

# The definite integral of f(x) * dx from 0 to 6 is equal to the definite integral of f(x) * dx from 0 to 2 + the definite integral of f(x) * dx from 2 to 5 + the definite integral of f(x) * dx from 5 to 6
# The definite integral of f(-4) * dx from 0 to 2 + the definite integral of f(x) * dx from 2 to 5 + the definite integral of f(-3) * dx from 5 to 6
# = (-4) * (2 - 0) + the definite integral of f(x) * dx from 2 to 5 + (-3) * (6 - 5)
# The definite integral of f(x) * dx from 0 to 2 is equal to -4 * 2 = -8
# The definite integral of f(x) * dx from 2 to 5 is equal to 1/2 * 5^2 - 1/2 * 2^2 = 11.5
# The definite integral of f(x) * dx from 5 to 6 is equal to -3 * 1 = -3

# Find the definite integral of f(x) * dx from 2 to 5
# Graph f(x) = x from 2 to 5
# Area is 1/2 * base * height
# A = 1/2 * 3 * 3 = 4.5
