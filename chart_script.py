# Create a better laid out flowchart using plotly with improved spacing and readability
import plotly.graph_objects as go
import numpy as np

# Define the nodes with better hierarchical positioning
nodes = {
    'Start': (6, 10),
    'Install Anaconda': (6, 9),
    'Install Deps': (6, 8),
    'Config Project': (6, 7),
    'Ready to train?': (6, 6),
    'Run train.py': (6, 5),
    'PPO Algorithm': (6, 4),
    'Model Saved': (6, 3),
    'Run test.py': (6, 2),
    'Visualize': (6, 1),
    'Analyze Perf': (6, 0),
    'Good results?': (6, -1),
    'Modify Config': (3, 3),
    'Write Report': (9, -1),
    'End': (9, -2)
}

# Define connections with clearer paths
connections = [
    ('Start', 'Install Anaconda'),
    ('Install Anaconda', 'Install Deps'),
    ('Install Deps', 'Config Project'),
    ('Config Project', 'Ready to train?'),
    ('Ready to train?', 'Run train.py'),
    ('Run train.py', 'PPO Algorithm'),
    ('PPO Algorithm', 'Model Saved'),
    ('Model Saved', 'Run test.py'),
    ('Run test.py', 'Visualize'),
    ('Visualize', 'Analyze Perf'),
    ('Analyze Perf', 'Good results?'),
    ('Good results?', 'Write Report'),
    ('Write Report', 'End')
]

# Add curved connections for loops
loop_connections = [
    ('Ready to train?', 'Config Project'),  # No loop back
    ('Good results?', 'Modify Config'),     # No loop to modify
    ('Modify Config', 'Run train.py')       # Back to training
]

# Color mapping for different stages
stage_colors = {
    # Start/End (gray)
    'Start': '#F0F0F0',
    'End': '#F0F0F0',
    
    # Setup (blue) 
    'Install Anaconda': '#87CEEB',
    'Install Deps': '#87CEEB', 
    'Config Project': '#87CEEB',
    
    # Training (orange)
    'Ready to train?': '#FFB347',
    'Run train.py': '#FFB347',
    'PPO Algorithm': '#FFB347',
    'Model Saved': '#FFB347',
    'Modify Config': '#FFB347',
    
    # Testing (green)
    'Run test.py': '#90EE90',
    'Visualize': '#90EE90',
    
    # Analysis (purple)
    'Analyze Perf': '#DDA0DD',
    'Good results?': '#DDA0DD',
    'Write Report': '#DDA0DD'
}

# Create the figure
fig = go.Figure()

# Add main flow edges
edge_x = []
edge_y = []
for connection in connections:
    x0, y0 = nodes[connection[0]]
    x1, y1 = nodes[connection[1]]
    edge_x.extend([x0, x1, None])
    edge_y.extend([y0, y1, None])

fig.add_trace(go.Scatter(
    x=edge_x, y=edge_y,
    line=dict(width=2, color='#888'),
    hoverinfo='none',
    mode='lines',
    showlegend=False
))

# Add loop edges with different style
loop_edge_x = []
loop_edge_y = []
for connection in loop_connections:
    x0, y0 = nodes[connection[0]]
    x1, y1 = nodes[connection[1]]
    loop_edge_x.extend([x0, x1, None])
    loop_edge_y.extend([y0, y1, None])

fig.add_trace(go.Scatter(
    x=loop_edge_x, y=loop_edge_y,
    line=dict(width=2, color='#FF6B6B', dash='dash'),
    hoverinfo='none',
    mode='lines',
    showlegend=False
))

# Add nodes with better sizing
node_x = [nodes[node][0] for node in nodes]
node_y = [nodes[node][1] for node in nodes]
node_colors = [stage_colors[node] for node in nodes]
node_text = list(nodes.keys())

fig.add_trace(go.Scatter(
    x=node_x, y=node_y,
    mode='markers+text',
    marker=dict(
        size=40,  # Larger nodes
        color=node_colors,
        line=dict(width=2, color='#333')
    ),
    text=node_text,
    textposition="middle center",
    textfont=dict(size=9, color='black'),
    hoverinfo='text',
    hovertext=node_text,
    showlegend=False
))

# Add decision labels with better positioning
fig.add_annotation(
    x=4.5, y=6.5,
    text='No',
    showarrow=True,
    arrowhead=2,
    arrowsize=1,
    arrowwidth=2,
    arrowcolor='#FF6B6B',
    ax=6, ay=6,
    font=dict(size=12, color='red')
)

fig.add_annotation(
    x=7.5, y=5.5,
    text='Yes',
    showarrow=True,
    arrowhead=2,
    arrowsize=1,
    arrowwidth=2,
    arrowcolor='#32CD32',
    ax=6, ay=6,
    font=dict(size=12, color='green')
)

fig.add_annotation(
    x=4.5, y=-0.5,
    text='No',
    showarrow=True,  
    arrowhead=2,
    arrowsize=1,
    arrowwidth=2,
    arrowcolor='#FF6B6B',
    ax=6, ay=-1,
    font=dict(size=12, color='red')
)

fig.add_annotation(
    x=7.5, y=-1,
    text='Yes',
    showarrow=True,
    arrowhead=2,
    arrowsize=1,
    arrowwidth=2,
    arrowcolor='#32CD32',
    ax=6, ay=-1,
    font=dict(size=12, color='green')
)

# Update layout with better spacing
fig.update_layout(
    title="AI Drone Project Workflow",
    showlegend=False,
    xaxis=dict(
        showgrid=False, 
        zeroline=False, 
        showticklabels=False,
        range=[0, 12]
    ),
    yaxis=dict(
        showgrid=False, 
        zeroline=False, 
        showticklabels=False,
        range=[-3, 11]
    ),
    plot_bgcolor='white',
    font=dict(size=12)
)

# Save the chart as both PNG and SVG
fig.write_image("ai_drone_workflow.png")
fig.write_image("ai_drone_workflow.svg", format="svg")
print("Improved flowchart saved successfully as PNG and SVG")