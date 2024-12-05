### RULE: Every problem must be solved through step-by-step using Calculus while providing the name of the concept used. ###
### RULE: Work every problem to completion step-by-step before you provide code. ###
### RULE: Work the problem through as if you're teaching someone in a Calculus class. ###
### RULE: Create plotly interactive graphics and video to deeply elaborate the steps and visualize concepts and provide the utmost clarification. ###
### RULE: Don't just keep adding steps. You MUST come to a definitive answer and stopping point. Think carefully to determine if the problem has been solved. ###
### RULE: Create DESMOS INPUTS: and follow up with EXPLAIN THE GRAPH: ###
### RULE: If a problem is complex, break it down into manageable parts. ###

# Let f(x) = sqrt8(x) - 8x for x > 0.
# Find the open intervals on which f is increasing or decreasing.
# Then determine all relative extrema of f.

# 1. f is increasing on invevals:
## (0, 1/4) 

# 2. f is decreasing on intervals:
## (1/4, infinity)

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Step 1: Define the function f(x) = sqrt(8x) - 8x
def f(x):
    return np.sqrt(8*x) - 8*x

# Step 2: Define the derivative f'(x) = 4/sqrt(8x) - 8
def f_prime(x):
    return 4/np.sqrt(8*x) - 8

# Create visualization
x = np.linspace(0.01, 2, 1000)
y = f(x)
y_prime = f_prime(x)

# Plot setup
plt.figure(figsize=(12, 8))
plt.subplot(2, 1, 1)
plt.plot(x, y, 'b-', label='f(x) = sqrt(8x) - 8x')
plt.axvline(x=1/4, color='r', linestyle='--', label='x = 1/4')
plt.grid(True)
plt.legend()
plt.title('Function f(x) and its Critical Point')

plt.subplot(2, 1, 2)
plt.plot(x, y_prime, 'g-', label="f'(x)")
plt.axhline(y=0, color='k', linestyle='-', alpha=0.3)
plt.axvline(x=1/4, color='r', linestyle='--', label='x = 1/4')
plt.grid(True)
plt.legend()
plt.title('Derivative f\'(x)')

plt.tight_layout()
plt.show()

# Add Plotly Interactive Visualization
def create_plotly_visualization():
    x_plotly = np.linspace(0.01, 2, 1000)
    y_plotly = f(x_plotly)
    y_prime_plotly = f_prime(x_plotly)
    
    fig = make_subplots(rows=2, cols=1,
                        subplot_titles=('Function f(x) and its Critical Point',
                                      'Derivative f\'(x)'))
    
    # Add traces for the function
    fig.add_trace(
        go.Scatter(x=x_plotly, y=y_plotly, name='f(x) = sqrt(8x) - 8x',
                  line=dict(color='blue')),
        row=1, col=1
    )
    
    # Add vertical line at x = 1/4
    fig.add_trace(
        go.Scatter(x=[0.25, 0.25], 
                  y=[min(y_plotly), max(y_plotly)],
                  name='x = 1/4',
                  line=dict(color='red', dash='dash')),
        row=1, col=1
    )
    
    # Add trace for the derivative
    fig.add_trace(
        go.Scatter(x=x_plotly, y=y_prime_plotly, name="f'(x)",
                  line=dict(color='green')),
        row=2, col=1
    )
    
    # Add horizontal line at y = 0 for derivative
    fig.add_trace(
        go.Scatter(x=[min(x_plotly), max(x_plotly)], y=[0, 0],
                  line=dict(color='black', width=0.5),
                  showlegend=False),
        row=2, col=1
    )
    
    # Add vertical line at x = 1/4 for derivative
    fig.add_trace(
        go.Scatter(x=[0.25, 0.25],
                  y=[min(y_prime_plotly), max(y_prime_plotly)],
                  name='x = 1/4',
                  line=dict(color='red', dash='dash')),
        row=2, col=1
    )
    
    fig.update_layout(
        height=800,
        showlegend=True,
        title_text="Interactive Visualization of f(x) and f'(x)"
    )
    
    # Add grid to both subplots
    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')
    
    fig.show()

# Call the Plotly visualization after matplotlib
create_plotly_visualization()

# DESMOS INPUTS:
# f(x)=\sqrt{8x}-8x
# f'(x)=\frac{4}{\sqrt{8x}}-8

"""
SOLUTION EXPLANATION:
1. To find intervals of increase/decrease, we analyze f'(x):
   f'(x) = 4/sqrt(8x) - 8
   
2. Set f'(x) = 0 and solve:
   4/sqrt(8x) - 8 = 0
   4/sqrt(8x) = 8
   4 = 8sqrt(8x)
   1/4 = x

3. Critical point is x = 1/4

4. Test intervals:
   - For 0 < x < 1/4: f'(x) > 0, so f is increasing
   - For x > 1/4: f'(x) < 0, so f is decreasing

5. Relative extrema:
   At x = 1/4, f has a relative maximum
   f(1/4) = sqrt(8(1/4)) - 8(1/4) = sqrt(2) - 2

EXPLAIN THE GRAPH:
- The top graph shows f(x) with a peak at x = 1/4
- The bottom graph shows f'(x) crossing zero at x = 1/4
- The dashed red line shows the critical point x = 1/4
- When f'(x) > 0, f(x) increases
- When f'(x) < 0, f(x) decreases
"""

