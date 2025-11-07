import plotly.graph_objects as go
import numpy as np
import plotly.io as pio

# Create a circular flowchart using plotly
fig = go.Figure()

# Define the 5 main components and their positions in a circle
components = [
    "Environment (drone_env.py)<br>State: position, velocity, goal distance",
    "AI Agent (PPO)<br>Neural Network Policy", 
    "Action<br>velocity commands [vx, vy, vz]",
    "Environment updates<br>Physics simulation steps",
    "Reward Calculation<br>+200 goal, -100 collision, -dist"
]

# Colors for each component type
colors = ['#B3E5EC', '#A5D6A7', '#FFEB8A', '#B3E5EC', '#FFCDD2']
border_colors = ['#1FB8CD', '#2E8B57', '#D2BA4C', '#1FB8CD', '#DB4545']

# Position nodes in a circle
n_nodes = len(components)
angles = np.linspace(0, 2*np.pi, n_nodes, endpoint=False)
radius = 1.5
x_positions = radius * np.cos(angles)
y_positions = radius * np.sin(angles)

# Add nodes
for i, (x, y, component, color, border_color) in enumerate(zip(x_positions, y_positions, components, colors, border_colors)):
    fig.add_trace(go.Scatter(
        x=[x], y=[y],
        mode='markers+text',
        marker=dict(size=120, color=color, line=dict(width=3, color=border_color)),
        text=component,
        textposition='middle center',
        textfont=dict(size=10),
        showlegend=False,
        hoverinfo='none'
    ))

# Add arrows between nodes
arrow_props = dict(arrowhead=2, arrowsize=1, arrowwidth=3, arrowcolor='#333333')
for i in range(n_nodes):
    start_x, start_y = x_positions[i], y_positions[i]
    end_x, end_y = x_positions[(i+1) % n_nodes], y_positions[(i+1) % n_nodes]
    
    # Calculate arrow position (slightly inward from node edges)
    dx, dy = end_x - start_x, end_y - start_y
    length = np.sqrt(dx**2 + dy**2)
    dx_norm, dy_norm = dx/length, dy/length
    
    arrow_start_x = start_x + 0.3 * dx_norm
    arrow_start_y = start_y + 0.3 * dy_norm
    arrow_end_x = end_x - 0.3 * dx_norm
    arrow_end_y = end_y - 0.3 * dy_norm
    
    fig.add_annotation(
        x=arrow_end_x, y=arrow_end_y,
        ax=arrow_start_x, ay=arrow_start_y,
        xref='x', yref='y',
        axref='x', ayref='y',
        arrowhead=2, arrowsize=1.5, arrowwidth=3, arrowcolor='#333333',
        showarrow=True
    )

# Add center label
fig.add_trace(go.Scatter(
    x=[0], y=[0],
    mode='markers+text',
    marker=dict(size=100, color='#f9f9f9', line=dict(width=2, color='#333333')),
    text="RL Training Loop<br>Repeats 150,000 times",
    textposition='middle center',
    textfont=dict(size=12, color='#333333'),
    showlegend=False,
    hoverinfo='none'
))

# Update layout
fig.update_layout(
    title="RL Training Loop - Drone Environment",
    xaxis=dict(showgrid=False, zeroline=False, showticklabels=False, range=[-2.5, 2.5]),
    yaxis=dict(showgrid=False, zeroline=False, showticklabels=False, range=[-2.5, 2.5]),
    plot_bgcolor='white',
    showlegend=False
)

# Save as PNG and SVG
fig.write_image("rl_training_loop.png")
fig.write_image("rl_training_loop.svg", format="svg")

print("Chart saved as PNG: rl_training_loop.png")
print("Chart saved as SVG: rl_training_loop.svg")