# Came in at 6:27pm

## Example1:
## Find definite integral of f(x) = sqrt(x) dx from 0 to 4

## Find the anti-derivative of swuare root of x or x^(1/2)

## f(x) = x^(1/2)
## F(x) = (2/3)x^(3/2)

## F(4) - F(0) = (2/3)(4)^(3/2) - (2/3)(0)^(3/2)
## = (2/3)(8) - (2/3)(0)
## = 16/3

## Recall we estimated the area under the curve y = sqrt(x) from 0 to 4
## 4 approximated rectangles and 
## (a) right endpoints
## (b) left endpoints
## (c) midpoints

## Found best estimate was 5.3838 using midpoints close to actual 16/3 ~ 5.3333

## So in above example, since 2/3x^(3/2) is anti-derivative of x^(1/2) or sqrt(x),
## the definite integral of sqrt(x)dx = 2/3x^(3/2) evaluated from 0 to 4 = 16/3

## Example2:
## Find the definite integral of f(x) = dx from 0 to 5 if,
## f(x) = { 3cos(x) if 0 <= x < pi }, { (x^5 + x^2)/x^2 if x >= pi }

## Use property 5 from 5.2 to rewrite the definite integral of f(x)dx from 0 to 5 as
## definite integral of f1(x)dx from 0 to pi + definite integral of f2(x)dx from pi to 5
## = the definite integral of 3cos(x)dx from 0 to pi + the definite integral of (x^5 + x^2)/x^2 dx from pi to 5

## 1. Find the anti-derivative of 3cos(x) or f1(x) = 3cos(x)
## F1(x) = 3sin(x) ---> (since anti-derivative of cos(x) is sin(x))
## F1(pi) - F1(0) = 3sin(pi) - 3sin(0) = 3(0) - 3(0) = 0

## 2. Find the anti-derivative of (x^5 + x^2)/x^2 
## NOTE: the integral of a quotient is NOT the quotient of the integrals
## = the integral of x^5/x^2 + x^2/x^2
## = the integral of x^3 + 1
## = x^4/4
## = x^4/4 + x

## So the definite integral of (x^5 + x^2)/x^2 dx from pi to 5
## = x^4/4 + x evaluated from pi to 5
## = (5^4/4 + 5) - (pi^4/4 + pi)
## = (625/4 + 5) - (pi^4/4 + pi)
## = (625/4 + 20/4) - (pi^4/4 + 4pi/4)
## = 645/4 - (pi^4 + 4pi)/4
## = (645 - pi^4 - 4pi)/4 ---> Simplified form
## NOTE: we calculated the definite integral of cos(x) from 0 to pi as 0
## Can confirm by graphing cos(x) from 0 to pi and finding the area under the curve

## Create matplotlib of cos(x) from 0 to pi
import numpy as np
import matplotlib.pyplot as plt

def plot_cosine():
    x = np.linspace(0, np.pi, 100)
    y = np.cos(x)
    
    plt.plot(x, y, 'b-', label='cos(x)')
    plt.fill_between(x, y, color='lightblue')
    
    plt.xlabel('x')
    plt.ylabel('cos(x)')
    plt.title('Graph of cos(x) from 0 to pi')
    plt.grid(True)
    plt.legend()
    
    plt.show()

if __name__ == "__main__":
    plot_cosine()
    