import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

def plot_area_function():
    # Create figure with two subplots
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 12))
    fig.suptitle('Maximizing Rectangle Area with Fixed Perimeter', fontsize=14)

    # Plot 1: Area as a function of width
    w = np.linspace(0, 20, 200)
    A = 40*w - 2*w**2

    ax1.plot(w, A, 'b-', label='A = 40w - 2w²')
    ax1.plot(10, 200, 'ro', label='Maximum Point (10, 200)')
    
    ax1.set_xlabel('Width (w)')
    ax1.set_ylabel('Area (A)')
    ax1.set_title('Area vs Width')
    ax1.grid(True)
    ax1.legend()

    # Add annotation for maximum point
    ax1.annotate('Maximum Area: 200 sq units\nw = 10, l = 20',
                xy=(10, 200), xytext=(12, 150),
                arrowprops=dict(facecolor='black', shrink=0.05))

    # Plot 2: Visual representation of the optimal rectangle
    ax2.set_xlim(-5, 25)
    ax2.set_ylim(-5, 15)
    ax2.grid(True)
    
    # Draw the wall
    ax2.plot([0, 0], [-2, 12], 'k-', linewidth=3, label='Wall')
    
    # Draw the optimal rectangle
    rect = Rectangle((0, 0), 20, 10, fill=False, color='blue', linewidth=2)
    ax2.add_patch(rect)
    
    # Add dimensions
    ax2.arrow(0, -1, 20, 0, head_width=0.3, head_length=0.5, fc='k', ec='k')
    ax2.arrow(20, -1, -20, 0, head_width=0.3, head_length=0.5, fc='k', ec='k')
    ax2.text(10, -2, 'Length = 20', ha='center')
    
    ax2.arrow(21, 0, 0, 10, head_width=0.3, head_length=0.5, fc='k', ec='k')
    ax2.arrow(21, 10, 0, -10, head_width=0.3, head_length=0.5, fc='k', ec='k')
    ax2.text(22.5, 5, 'Width = 10', va='center')
    
    ax2.set_title('Optimal Rectangle Configuration')
    ax2.legend()
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    plot_area_function()
