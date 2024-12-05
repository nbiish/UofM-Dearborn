import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from mpl_toolkits.mplot3d import Axes3D

def plot_box_and_surface_area(V=100):  # Default volume of 100 cubic units
    # Create figure with two subplots
    fig = plt.figure(figsize=(15, 6))
    fig.suptitle('Box Optimization Problem (No Top)', fontsize=14)
    
    # First subplot: 3D box visualization
    ax1 = fig.add_subplot(121, projection='3d')
    
    # Calculate optimal dimensions
    x = (7*V/36)**(1/3)
    l = 6*x  # longer side
    h = V/(6*x**2)
    
    # Define vertices of the box (without top)
    vertices = np.array([
        [0, 0, 0],      # 0: bottom front left
        [l, 0, 0],      # 1: bottom front right
        [l, x, 0],      # 2: bottom back right
        [0, x, 0],      # 3: bottom back left
        [0, 0, h],      # 4: top front left
        [l, 0, h],      # 5: top front right
        [l, x, h],      # 6: top back right
        [0, x, h]       # 7: top back left
    ])
    
    # Define faces (5 faces, excluding top)
    faces = [
        [vertices[0], vertices[1], vertices[2], vertices[3]],  # bottom
        [vertices[0], vertices[1], vertices[5], vertices[4]],  # front
        [vertices[1], vertices[2], vertices[6], vertices[5]],  # right
        [vertices[2], vertices[3], vertices[7], vertices[6]],  # back
        [vertices[3], vertices[0], vertices[4], vertices[7]]   # left
    ]
    
    # Plot the faces
    ax1.add_collection3d(Poly3DCollection(faces, alpha=0.25, facecolor='blue'))
    
    # Set axis labels
    ax1.set_xlabel('Length (6x)')
    ax1.set_ylabel('Width (x)')
    ax1.set_zlabel('Height (h)')
    
    # Add dimensions as text
    ax1.text(l/2, -x/2, 0, f'Length = {l:.2f}', ha='center')
    ax1.text(l+x/2, x/2, 0, f'Width = {x:.2f}', ha='center')
    ax1.text(-x/2, x/2, h/2, f'Height = {h:.2f}', ha='center')
    
    # Set axis limits
    max_dim = max(l, x, h)
    ax1.set_xlim([-max_dim/4, l+max_dim/4])
    ax1.set_ylim([-max_dim/4, x+max_dim/4])
    ax1.set_zlim([0, h+max_dim/4])
    
    # Second subplot: Surface Area as function of x
    ax2 = fig.add_subplot(122)
    
    # Create x values for plotting
    x_vals = np.linspace(x/2, x*2, 100)
    
    # Calculate surface area for each x value
    A = 6*x_vals**2 + 7*V/(3*x_vals)
    
    # Plot surface area
    ax2.plot(x_vals, A, 'b-', label='Surface Area')
    ax2.plot(x, 6*x**2 + 7*V/(3*x), 'ro', label='Minimum Point')
    
    ax2.set_xlabel('Width (x)')
    ax2.set_ylabel('Surface Area')
    ax2.set_title('Surface Area vs Width')
    ax2.grid(True)
    ax2.legend()
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    plot_box_and_surface_area(100)  # Using volume = 100 as example
