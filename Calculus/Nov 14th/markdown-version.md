<!-- filepath: /Users/nbiish/code/Calculus/Nov 14th/markdown-version.md -->

<!-- RULE: WHEN CHANGING THIS MAKE SURE TO MAKE IT AN INSTRUCTIONAL FOR LEARNING THE STEPS -->
<!-- RULE: Make the instructional text larger -->
<!-- RULE: Format everything so that it's easier to view in an orderly fashion -->
<!-- RULE: Mainitain the variables and format the additional information added from examples.py -->

# EXAMPLE 1

**GIVE A LOT OF DETAIL AND WORK ME THROUGH EVERY STEP**

Find the most general antiderivative of the following function:

$$
f(x) = \frac{1}{x^7}
$$

## **Step 1: Rewrite the Function Using Negative Exponents**

Recall that:

$$
\frac{1}{x^n} = x^{-n}
$$

So, we can rewrite the function as:

$$
f(x) = x^{-7}
$$

## **Step 2: Apply the Power Rule for Integration**

The power rule for integration states:

$$
\int x^{n} \,dx = \frac{x^{n+1}}{n+1} + C, \quad \text{for } n \neq -1
$$

Applying the power rule to \( f(x) \):

$$
\begin{align*}
F(x) &= \int x^{-7} \,dx \\
&= \frac{x^{-7 + 1}}{-7 + 1} + C \\
&= \frac{x^{-6}}{-6} + C \\
&= -\frac{1}{6x^6} + C
\end{align*}
$$

## **Conclusion**

The most general antiderivative of \( f(x) = \frac{1}{x^7} \) is:

$$
F(x) = -\frac{1}{6x^6} + C
$$

where \( C \) is an arbitrary constant.

---

# EXAMPLE 2

Find the most general antiderivative of the following function:

$$
h(t) = \frac{8 - t^2}{t^{1/5}}
$$

**Note:** We cannot find the antiderivative of the numerator and denominator separately. The antiderivative of a quotient is **not** the quotient of the antiderivatives.

## **Step 1: Split the Fraction**

Express \( h(t) \) as two separate terms:

$$
h(t) = \frac{8}{t^{1/5}} - \frac{t^2}{t^{1/5}}
$$

## **Step 2: Simplify the Expression**

Rewrite each term using exponent rules.

For the first term:

$$
\frac{8}{t^{1/5}} = 8t^{-1/5}
$$

For the second term:

$$
t^2 \cdot t^{-1/5} = t^{2 - 1/5} = t^{\frac{10}{5} - \frac{1}{5}} = t^{\frac{9}{5}}
$$

So the function becomes:

$$
h(t) = 8t^{-1/5} - t^{9/5}
$$

## **Step 3: Apply the Power Rule for Integration**

1. **Antiderivative of \( 8t^{-1/5} \):**

   $$
   \begin{align*}
   \int 8t^{-1/5} \,dt &= 8 \int t^{-1/5} \,dt \\
   &= 8 \left( \frac{t^{-1/5 + 1}}{-1/5 + 1} \right) + C \\
   &= 8 \left( \frac{t^{4/5}}{4/5} \right) + C \\
   &= 8 \left( \frac{5}{4} t^{4/5} \right) + C \\
   &= 10 t^{4/5} + C
   \end{align*}
   $$

2. **Antiderivative of \( -t^{9/5} \):**

   $$
   \begin{align*}
   \int -t^{9/5} \,dt &= -\int t^{9/5} \,dt \\
   &= -\left( \frac{t^{9/5 + 1}}{9/5 + 1} \right) + C \\
   &= -\left( \frac{t^{14/5}}{14/5} \right) + C \\
   &= -\left( \frac{5}{14} t^{14/5} \right) + C
   \end{align*}
   $$

## **Step 4: Combine the Results**

$$
H(t) = 10 t^{4/5} - \frac{5}{14} t^{14/5} + C
$$

where \( C \) is an arbitrary constant.

## **Conclusion**

The most general antiderivative of \( h(t) = \frac{8 - t^2}{t^{1/5}} \) is:

$$
H(t) = 10 t^{4/5} - \frac{5}{14} t^{14/5} + C
$$

---

# EXAMPLE 3 (from #16 on page 355 in the book)

Find the most general antiderivative of the following function:

$$
r(\theta) = 2e^{\theta} \sec(\theta) \tan(\theta)
$$

## **Step 1: Recognize the Derivative of \( \sec(\theta) \)**

Recall that:

$$
\frac{d}{d\theta} [\sec(\theta)] = \sec(\theta) \tan(\theta)
$$

## **Step 2: Use Substitution**

Let:

$$
u = \sec(\theta)
$$

Then:

$$
du = \sec(\theta) \tan(\theta) \, d\theta
$$

## **Step 3: Rewrite the Integral**

Express the integral in terms of \( u \):

$$
\int r(\theta) \, d\theta = \int 2e^{\theta} \sec(\theta) \tan(\theta) \, d\theta = 2 \int e^{\theta} \, du
$$

## **Step 4: Integrate with Respect to \( u \)**

Since \( e^{\theta} \) is a function of \( \theta \), and we are integrating with respect to \( u \), we need to express \( e^{\theta} \) in terms of \( u \). However, without a direct relationship between \( e^{\theta} \) and \( u \), this substitution approach becomes complex.

## **Step 5: Observe a Pattern**

Consider the derivative of \( 2 e^{\theta} \sec(\theta) \):

$$
\frac{d}{d\theta} [2 e^{\theta} \sec(\theta)] = 2 e^{\theta} \sec(\theta) + 2 e^{\theta} \sec(\theta) \tan(\theta)
$$

Notice that:

$$
2 e^{\theta} \sec(\theta) \tan(\theta) = \frac{d}{d\theta} [2 e^{\theta} \sec(\theta)] - 2 e^{\theta} \sec(\theta)
$$

## **Step 6: Integrate Both Sides**

Integrate both sides with respect to \( \theta \):

$$
\int 2 e^{\theta} \sec(\theta) \tan(\theta) \, d\theta = \int \left( \frac{d}{d\theta} [2 e^{\theta} \sec(\theta)] - 2 e^{\theta} \sec(\theta) \right) \, d\theta
$$

Simplify:

$$
\int 2 e^{\theta} \sec(\theta) \tan(\theta) \, d\theta = 2 e^{\theta} \sec(\theta) - 2 \int e^{\theta} \sec(\theta) \, d\theta + C
$$

## **Step 7: Solve for the Integral**

Rearrange the equation to solve for \( \int e^{\theta} \sec(\theta) \, d\theta \):

Let \( I = \int e^{\theta} \sec(\theta) \, d\theta \). Then:

$$
\int 2 e^{\theta} \sec(\theta) \tan(\theta) \, d\theta = 2 e^{\theta} \sec(\theta) - 2I + C
$$

This leads to:

$$
I = e^{\theta} \sec(\theta) + C
$$

Therefore, the antiderivative of \( r(\theta) \) is:

$$
R(\theta) = 2 e^{\theta} \sec(\theta) + C
$$

## **Conclusion**

The most general antiderivative of \( r(\theta) = 2e^{\theta} \sec(\theta) \tan(\theta) \) is:

$$
R(\theta) = 2 e^{\theta} \sec(\theta) + C
$$

where \( C \) is an arbitrary constant.

---

# EXAMPLE 4

Find \( f \) if \( f'(x) = x^{1/3}(4 + 14x) \) and \( f(1) = 5 \).

## **Step 1: Expand the Expression**

Multiply \( x^{1/3} \) with each term inside the parentheses:

$$
f'(x) = 4 x^{1/3} + 14 x^{1/3} \cdot x = 4 x^{1/3} + 14 x^{1/3 + 1} = 4 x^{1/3} + 14 x^{4/3}
$$

## **Step 2: Apply the Power Rule for Integration**

Integrate each term separately.

1. **Antiderivative of \( 4 x^{1/3} \):**

   $$
   \begin{align*}
   \int 4 x^{1/3} \,dx &= 4 \int x^{1/3} \,dx \\
   &= 4 \left( \frac{x^{1/3 + 1}}{1/3 + 1} \right) + C \\
   &= 4 \left( \frac{x^{4/3}}{4/3} \right) + C \\
   &= 4 \left( \frac{3}{4} x^{4/3} \right) + C \\
   &= 3 x^{4/3} + C
   \end{align*}
   $$

2. **Antiderivative of \( 14 x^{4/3} \):**

   $$
   \begin{align*}
   \int 14 x^{4/3} \,dx &= 14 \int x^{4/3} \,dx \\
   &= 14 \left( \frac{x^{4/3 + 1}}{4/3 + 1} \right) + C \\
   &= 14 \left( \frac{x^{7/3}}{7/3} \right) + C \\
   &= 14 \left( \frac{3}{7} x^{7/3} \right) + C \\
   &= 6 x^{7/3} + C
   \end{align*}
   $$

## **Step 3: Combine the Results**

$$
f(x) = 3 x^{4/3} + 6 x^{7/3} + C
$$

## **Step 4: Use the Initial Condition \( f(1) = 5 \) to Solve for \( C \)**

Substitute \( x = 1 \) and \( f(1) = 5 \):

$$
5 = 3 (1)^{4/3} + 6 (1)^{7/3} + C = 3 + 6 + C = 9 + C
$$

Solve for \( C \):

$$
C = 5 - 9 = -4
$$

## **Conclusion**

The function \( f \) is:

$$
f(x) = 3 x^{4/3} + 6 x^{7/3} - 4
$$

---

# EXAMPLE 5

Find \( f \) if \( f''(x) = \pi \), \( f'(0) = 1 \), and \( f(4) = 7 \).

## **Step 1: Integrate \( f''(x) \) to Find \( f'(x) \)**

Given:

$$
f''(x) = \pi
$$

Integrate \( f''(x) \) with respect to \( x \):

$$
\int f''(x) \,dx = \int \pi \,dx
$$

Thus,

$$
f'(x) = \pi x + C_1
$$

where \( C_1 \) is the constant of integration.

## **Step 2: Use the Initial Condition \( f'(0) = 1 \) to Find \( C_1 \)**

Substitute \( x = 0 \) and \( f'(0) = 1 \):

$$
1 = \pi (0) + C_1 \\
1 = 0 + C_1 \\
C_1 = 1
$$

So,

$$
f'(x) = \pi x + 1
$$

## **Step 3: Integrate \( f'(x) \) to Find \( f(x) \)**

Integrate \( f'(x) \) with respect to \( x \):

$$
\int f'(x) \,dx = \int (\pi x + 1) \,dx
$$

Thus,

$$
f(x) = \frac{\pi}{2} x^2 + x + C_2
$$

where \( C_2 \) is the constant of integration.

## **Step 4: Use the Initial Condition \( f(4) = 7 \) to Find \( C_2 \)**

Substitute \( x = 4 \) and \( f(4) = 7 \):

$$
7 = \frac{\pi}{2} (4)^2 + 4 + C_2 \\
7 = \frac{\pi}{2} \cdot 16 + 4 + C_2 \\
7 = 8\pi + 4 + C_2 \\
C_2 = 7 - 8\pi - 4 \\
C_2 = 3 - 8\pi
$$

## **Conclusion**

The function \( f \) is:

$$
f(x) = \frac{\pi}{2} x^2 + x + 3 - 8\pi
$$

---
