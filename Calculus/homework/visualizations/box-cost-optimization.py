import numpy as np
import dash
from dash import dcc, html, Input, Output
import plotly.graph_objects as go

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div([
    html.H1("Cost Optimization for Box with Open Top"),
    
    # Slider for volume V
    html.Label("Volume (V) in cubic meters"),
    dcc.Slider(
        id='volume-slider',
        min=1, max=100, step=1, value=10,
        marks={1: '1', 10: '10', 25: '25', 50: '50', 100: '100'}
    ),
    
    # 3D plot
    dcc.Graph(id='cost-optimization-graph')
])

# Define the callback to update the graph based on the volume
@app.callback(
    Output('cost-optimization-graph', 'figure'),
    Input('volume-slider', 'value')
)
def update_graph(volume):
    # Define a range for length L, avoiding too large or too small values
    L_values = np.linspace(5, 50, 100)  # Length values from 5 to 50
    
    # Calculate W and H in terms of L and V
    W_values = np.sqrt((6 * volume) / (5 * L_values))
    H_values = volume / (L_values * W_values)
    
    # Calculate cost C using the formula C = 10LW + 12WH + 12LH
    C_values = 10 * L_values * W_values + 12 * W_values * H_values + 12 * L_values * H_values
    
    # Replace any NaN or infinite values in C_values with 0
    C_values = np.nan_to_num(C_values, nan=0, posinf=0, neginf=0)
    
    # Create the 3D surface plot
    fig = go.Figure(data=[
        go.Surface(
            x=L_values, y=W_values, z=C_values,
            colorscale="Viridis", colorbar=dict(title="Cost")
        )
    ])
    
    # Update layout for better readability
    fig.update_layout(
        title=f"Cost Optimization (Volume V = {volume})",
        scene=dict(
            xaxis_title="Length (L)",
            yaxis_title="Width (W)",
            zaxis_title="Cost (C)"
        )
    )
    
    return fig

# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)