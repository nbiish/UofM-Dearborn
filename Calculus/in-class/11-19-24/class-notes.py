## RULE: Deeply explain and solve step-by-step


# EXAMPLE 1:
# Estimate area under the curve f(x) = sqrt(x) from x = 0 to x = 4 using 4 approximating rectangles and...
# (a) right endpoints
# (b) left endpoints
# (c) midpoints

# (a) right endpoints
# Width of each rectangle is delta x = (b-a)/n = (length of interval)/(number of rectangles) = (4-0)/4 = 1

# R_4 = f(1) + f(2) + f(3) + f(4)
#     = sqrt(1) + sqrt(2) + sqrt(3) + sqrt(4)
#     = 1 + sqrt(2) + sqrt(3) + 2
#     = 1 + 1.41 + 1.73 + 2
#     = 6.1463 (approx) <-- Overestimate of actual area based on graph

# (b) left endpoints
# L_4 = f(0) + f(1) + f(2) + f(3)
#     = sqrt(0) + sqrt(1) + sqrt(2) + sqrt(3)
#     = 0 + 1 + 1.41 + 1.73
#     = 4.14 (approx) <-- Underestimate of actual area based on graph

# (c) midpoints
# M_4 = f(0.5) + f(1.5) + f(2.5) + f(3.5)
#     = sqrt(0.5) + sqrt(1.5) + sqrt(2.5) + sqrt(3.5)
#     = 0.71 + 1.22 + 1.58 + 1.87
#     = 5.38 (approx) <-- Closer to actual area based on graph

# Create a graph to visualize the area under the curve