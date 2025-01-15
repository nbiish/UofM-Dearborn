### EXAMPLE 1 ###
### GIVE A LOT OF DETAIL AND WORK ME THROUGH EVERY STEP ###
#Find the most general antiderivative of the following function:
# f(x) = (1/x^^7) 

# First find a particular antiderivative of f(x) = 1/x^7.

# The antiderivative of f(x) = 1/x^7 is F(x) = -1/(6x^6) + C, where C is an arbitrary constant. 

# Now, we will find the most general antiderivative of f(x) = 1/x^7.

# The most general antiderivative of f(x) = 1/x^7 is F(x) = -1/(6x^6) + C, where C is an arbitrary constant.

### EXAMPLE 2 ###

#Find the most general antiderivative of the following function:
# h(t) = (8-t^2)/(t^(1/5)))

# NOTE # Cannot find antiderivative of numerator and demoninator. Antiderivative of quotient is NOT the quotient of the antiderivatives.

# Split up the fraction

# h(t) = 8/(t^(1/5)) - t^2/(t^(1/5))

# Simplify the expression 

# h(t) = 8t^(-1/5) - t^(2 - 1/5) -------- ####Question: what does t^(2 - 1/5) simplify to? answer: t^(9/5)

# h(t) = 8t^(-1/5) - t^(9/5)

# Find the antiderivative of h(t) = 8t^(-1/5) - t^(9/5)

# The antiderivative of h(t) = 8t^(-1/5) - t^(9/5) is H(t) = 40t^(4/5) - (5/14)t^(14/5) + C, where C is an arbitrary constant.

# Now, we will find the most general antiderivative of h(t) = (8-t^2)/(t^(1/5)).

# The most general antiderivative of h(t) = (8-t^2)/(t^(1/5)) is H(t) = 40t^(4/5) - (5/14)t^(14/5) + C, where C is an arbitrary constant.

### EXAMPLE 3 ### (from #16 on page 355 in book)

# Most general antiderivative of r(theta) = sec(theta)tan(theta)*2e^(theta)

# First, we will find a particular antiderivative of r(theta) = sec(theta)tan(theta)*(2e^(theta)).

# The antiderivative of r(theta) = sec(theta)tan(theta)*(2e^(theta)) is R(theta) = sec(theta) - 2e^(theta) + C, where C is an arbitrary constant.

# Now, we will find the most general antiderivative of r(theta) = sec(theta)tan(theta)*(2e^(theta)).

# Check the derivative of R(theta) = sec(theta) - 2e^(theta) + C

# d/d(theta) [sec(theta) - 2e^(theta) + C] = sec(theta)tan(theta) - 2e^(theta)

# NOTE # A ***differential equation*** is an equation containing derivatives.

### EXAMPLE 4 ### Find f is F'(x) = x^(1/3) * (4+14x) and f(1) = 5.

# First, we will find a particular antiderivative of F'(x) = x^(1/3) * (4+14x).

# Note # antiderivative of product is NOT the product of the antiderivatives.

# Andi-derivative of F'(x) = x^(1/3) * (4+14x) is F(x) = 3/4x^(4/3) + 6x^(7/3) + (-4)

# = 3/4x^(4/3) + 6x^(7/3) - 4

### EXAMPLE 5 ### Find f if f''(x) = pi, f'(0) = 1, f(4) = 7.

# f' is an antiderivative of f''

# antiderivative of pi is pi(x) (From special case of 1 since pi is a constant)

# So f'(x) = pi(x) + C, c arbitrat constant. Find c using f'(0) = 1

# f'(0) = pi(0) + C 

# 1 = 0 + C

# So f'(x) = pi(x) + 1

# f is an antiderivative of f'

# andtiderivative of pi(x)+1 is pi(x) * (x^2/2) + x

# So f(x) = pi(x) * (x^2/2) + x + D, D is arbitrary constant

# f(4) = pi(4) * (4^2/2) + 4 + D = 7

# 8pi + 4 + D = 7

# So D = 3 - 8pi

# So f(x) = pi(x) * (x^2/2) + x + 3 - 8pi

### Recall velocity is derivative of position function......and acceleration is derivative of velocity function

# So position is antiderivative of velocity function

# and acceleration is antiderivative of velocity function

# So velocity is antiderivative of acceleration function

### EXAMPLE 6 #62 from book ### 
# Find position function if
# a(t) = 3cos(t) - 3sin(t), s(0) = 0, v(0) = 4

# v(t) is antiderivative of a(t)
# 3sin(t) - 2(-cos(t)) + C
# 3sin(t) + 3cos(t) + C
# v(0) = 4 
# v(t) = 3sin(t) + 3cos(t) + 