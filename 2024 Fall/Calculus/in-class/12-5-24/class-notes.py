# <EXAMPLE1>:
# Find definite integral of sec(t)(sec(t) + tan(t)) dt 

## Note: integral of prodict is NOT product of integrals

# = definite integral of sec^2(t) + sec(t)tan(t) dt
# = definite integral of sec^2(t) dt + definite integral of sec(t)tan(t) dt
# = tan(t) + sec(t) + C ✅
# </EXAMPLE1>

# Net Change Theorem:
# The definite integral of a rate of change of a function equals the net change in the function...
# i.e.
# definite integral of f'(x) dx = f(b) - f(a) from a to b ✅

# If an object moves along a line and has position finction S(t), 

# we know V(t) = S'(t) ...
# is the velocity function and ...

# A(t) = V'(t) ...
# is the acceleration function

# So the definite integral of V(t) dt from t_1 to t_2 = definite integral of S'(t) dt from t_1 to t_2 = S(t_2) - S(t_1) --- (by Net Change Theorem)
# and is the net change in position from t_1 to t_2, i.e. DISPLACEMENT
# Basically equals ending position minus starting position

# The definite integral of |V(t)| dt from t_1 to t_2 is the total distance traveled from t_1 to t_2
# traveled on time interval [t_1, t_2], regardless of wether travelling forward or backward.

# <EXAMPLE2>:
# Say that you walk forward 10 ft, then backwards 4 ft.
# Displacement = 10 - 4 = 6 ft
# but total distance traveled = 10 + 4 = 14 ft
# </EXAMPLE2>

# <EXAMPLE3>:
# Let v(t) = 2t-10 be velocity function (in m/sec) for a particle moving along a line on the time interval 0 <= t <= 7
# a) Find the displacement of the particle on the interval [0, 7]
# b) Find the total distance traveled by the particle on the interval [0, 7]
# c) Displacement = definite integral of v(t) dt from 0 to 7 = definite integral of (2t-10) dt from 0 to 7 = t^2 - 10t from 0 to 7
# = (7)^2 - 10(7) - (0)^2 - 10(0) 
# = 49 - 70 - 0 + 0 
# = -21 m

# b) Total distance travelled
# = definite integral of |v(t)| dt from 0 to 7 = definite integral of |2t-10| dt from 0 to 7
# Simplify to |2t-10| 

# Recall |x| = x {x if x >= 0, -x if x < 0}
# So |2t-10| = 2t-10 {2t-10 if 2t-10 >= 0 ---> (t >= 5), -(2t-10) if 2t-10 < 0 ---> (t < 5)}

# So break up integral into two smaller integrals using 5 as the dividing point
# = definite integral of |2t-10| dt from 0 to 7 = definite integral of |2t-10| dt from 0 to 5 + definite integral of |2t-10| dt from 5 to 7
# (by Propert of Definite Integrals)
# = definite integral of (10-2t) dt from 0 to 5 + definite integral of (2t-10) dt from 5 to 7
# = 10t - t^2 from 0 to 5 + t^2 - 10t from 5 to 7
# = 10(5) - (5)^2 - (10(0) - (0)^2) + (7)^2 - 10(7) - ((5)^2 + 10(5))
# = 25 + 4
# = 29 m
# (Note: 29 m is the total distance traveled by the particle on the interval [0, 7])
# </EXAMPLE3>

# <EXAMPLE4>:
# Current in a wire is defined as derivative of the change in charge with respect to time.
# i.e. I(t) = dQ/dt or Q'(t) where Q(t) is the charge in the wire at time t.
# So current is the rate of change of charge with respect to time.

# What does the definite integral of I(t) dt from a to b represent?
# = definite integral of I(t) dt from a to b = definite integral of Q'(t) dt from a to b
# = definite integral of dQ/dt dt from a to b
# = definite integral of dQ from a to b
# = Q(b) - Q(a)
# = change in charge from a to b
# (Note: This is the net change in charge from a to b)

# What does the definite integral of |I(t)| dt from a to b represent?
# = definite integral of |I(t)| dt from a to b = definite integral of |Q'(t)| dt from a to b
# = definite integral of |dQ/dt| dt from a to b
# = definite integral of |dQ| from a to b
# = |Q(b) - Q(a)|
# = |change in charge from a to b|
# (Note: This is the total change in charge from a to b)
# </EXAMPLE4>

# Test content:
# 3.4 - 5.2