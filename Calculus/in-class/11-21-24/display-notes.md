# Calculus Notes

## Net Area and the Midpoint Rule

### Example 2: Net Area Calculation

**Problem**: Find the definite integral of \( f(x) = 2 - x \) from \( x = -1 \) to \( x = 3 \). Also, graph the function over this interval.

#### Solution:

1. **Graph the Function**:

   - The function \( f(x) = 2 - x \) is a straight line with a y-intercept at \( (0, 2) \) and a slope of \( -1 \).

   - **Desmos Input**: Copy and paste the following into [Desmos](https://www.desmos.com/calculator) to graph the function:

     ```
     f(x) = 2 - x
     ```

2. **Identify the Areas**:

   - The area under the curve from \( x = -1 \) to \( x = 3 \) consists of two triangular regions:
     - **\( A_1 \)**: Triangle above the x-axis (from \( x = -1 \) to \( x = 2 \)).
     - **\( A_2 \)**: Triangle below the x-axis (from \( x = 2 \) to \( x = 3 \)).

3. **Calculate \( A_1 \)**:

   - **Base**: \( 2 - (-1) = 3 \).
   - **Height**: \( f(-1) = 2 - (-1) = 3 \).
   - **Area**:
     \[
     A_1 = \dfrac{1}{2} \times \text{base} \times \text{height} = \dfrac{1}{2} \times 3 \times 3 = 4.5
     \]

4. **Calculate \( A_2 \)**:

   - **Base**: \( 3 - 2 = 1 \).
   - **Height**: \( |f(3)| = |2 - 3| = 1 \).
   - **Area**:
     \[
     A_2 = \dfrac{1}{2} \times \text{base} \times \text{height} = \dfrac{1}{2} \times 1 \times 1 = 0.5
     \]

5. **Calculate Net Area**:

   \[
   \text{Net Area} = A_1 - A_2 = 4.5 - 0.5 = 4
   \]

**Answer**: The definite integral \( \int_{-1}^{3} (2 - x) \, dx = 4 \).

---

### Example 3: Midpoint Rule Approximation

**Problem**: Use the Midpoint Rule with \( n = 4 \) to estimate the definite integral of \( f(x) = \dfrac{x}{\sqrt{1 + 2x}} \) from \( x = 1 \) to \( x = 3 \). Round your answer to three decimal places.

#### Solution:

1. **Calculate \( \Delta x \)**:

   \[
   \Delta x = \dfrac{b - a}{n} = \dfrac{3 - 1}{4} = 0.5
   \]

2. **Determine the Subintervals and Midpoints**:

   | Subinterval      | Midpoint (\( \bar{x}_i \))          |
   |------------------|-------------------------------------|
   | \( [1, 1.5] \)   | \( \dfrac{1 + 1.5}{2} = 1.25 \)     |
   | \( [1.5, 2] \)   | \( \dfrac{1.5 + 2}{2} = 1.75 \)     |
   | \( [2, 2.5] \)   | \( \dfrac{2 + 2.5}{2} = 2.25 \)     |
   | \( [2.5, 3] \)   | \( \dfrac{2.5 + 3}{2} = 2.75 \)     |

3. **Compute \( f(\bar{x}_i) \) for Each Midpoint**:

   - **Function**:
     \[
     f(x) = \dfrac{x}{\sqrt{1 + 2x}}
     \]
   - **Calculations**:

     | \( \bar{x}_i \) | \( f(\bar{x}_i) \)                            | Approximate Value |
     |-----------------|-----------------------------------------------|-------------------|
     | \( 1.25 \)      | \( \dfrac{1.25}{\sqrt{1 + 2 \times 1.25}} \)  | \( 0.668 \)       |
     | \( 1.75 \)      | \( \dfrac{1.75}{\sqrt{1 + 2 \times 1.75}} \)  | \( 0.823 \)       |
     | \( 2.25 \)      | \( \dfrac{2.25}{\sqrt{1 + 2 \times 2.25}} \)  | \( 0.959 \)       |
     | \( 2.75 \)      | \( \dfrac{2.75}{\sqrt{1 + 2 \times 2.75}} \)  | \( 1.080 \)       |

4. **Compute the Approximate Integral**:

   \[
   \int_{1}^{3} f(x) \, dx \approx \Delta x \left( f(\bar{x}_1) + f(\bar{x}_2) + f(\bar{x}_3) + f(\bar{x}_4) \right)
   \]
   \[
   \approx 0.5 \times (0.668 + 0.823 + 0.959 + 1.080) = 0.5 \times 3.530 = 1.765
   \]

**Answer**: The approximate value of the integral is **1.765**.

---

### Desmos Inputs for Visualization

To reinforce your understanding, you can visualize the function and the Midpoint Rule approximation using Desmos.

#### Steps:

1. **Graphing the Function**:

   - **Input**:
     ```
     f(x) = x / sqrt(1 + 2x)
     ```
   - **Description**: This graphs the function \( f(x) = \dfrac{x}{\sqrt{1 + 2x}} \) on Desmos.

2. **Plotting the Midpoints**:

   - **Define Midpoints**:
     ```
     x_1 = 1.25
     x_2 = 1.75
     x_3 = 2.25
     x_4 = 2.75
     ```
   - **Plot Points**:
     ```
     (x_1, f(x_1))
     (x_2, f(x_2))
     (x_3, f(x_3))
     (x_4, f(x_4))
     ```
   - **Description**: This plots the midpoint points used in the approximation.

3. **Drawing the Rectangles**:

   - **Rectangle Functions**:
     - **Rectangle 1**:
       ```
       R1(x) = {1 ≤ x ≤ 1.5} f(1.25)
       ```
     - **Rectangle 2**:
       ```
       R2(x) = {1.5 ≤ x ≤ 2} f(1.75)
       ```
     - **Rectangle 3**:
       ```
       R3(x) = {2 ≤ x ≤ 2.5} f(2.25)
       ```
     - **Rectangle 4**:
       ```
       R4(x) = {2.5 ≤ x ≤ 3} f(2.75)
       ```
   - **Input**: Enter the above piecewise functions into Desmos.
   - **Description**: These represent the tops of the rectangles for each subinterval.

4. **Shading the Rectangles**:

   - **Inequalities for Shading**:
     - **Rectangle 1**:
       ```
       0 ≤ y ≤ f(1.25) {1 ≤ x ≤ 1.5}
       ```
     - **Rectangle 2**:
       ```
       0 ≤ y ≤ f(1.75) {1.5 ≤ x ≤ 2}
       ```
     - **Rectangle 3**:
       ```
       0 ≤ y ≤ f(2.25) {2 ≤ x ≤ 2.5}
       ```
     - **Rectangle 4**:
       ```
       0 ≤ y ≤ f(2.75) {2.5 ≤ x ≤ 3}
       ```
   - **Input**: Enter these inequalities to shade the area under each rectangle.
   - **Description**: This visually demonstrates how the Midpoint Rule approximates the area under the curve.

---

### Additional Concepts

#### Reversing Limits of Integration

- **Property**:
  \[
  \int_{a}^{b} f(x) \, dx = -\int_{b}^{a} f(x) \, dx
  \]
- **Explanation**: Reversing the limits of integration changes the sign of the integral.

#### Zero Width Interval

- **Property**:
  \[
  \int_{a}^{a} f(x) \, dx = 0
  \]
- **Explanation**: The integral over an interval of zero width is zero because there is no area under the curve.

#### Properties of Definite Integrals

1. **Constant Multiple Rule**:

   - **Property**:
     \[
     \int_{a}^{b} c \, dx = c(b - a)
     \]
   - **Explanation**: The area under a constant function \( c \) from \( a \) to \( b \) is a rectangle with height \( c \) and width \( b - a \).
   - **Desmos Input**:
     ```
     y = c  (e.g., y = 2)
     ```
     - Adjust the value of \( c \) as needed.
     - Use sliders in Desmos to dynamically change \( c \), \( a \), and \( b \).

---

By working through these examples and visualizations, you'll gain a deeper understanding of definite integrals and the Midpoint Rule. Use the Desmos inputs to interactively explore the concepts.
