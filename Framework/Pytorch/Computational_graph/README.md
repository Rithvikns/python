
# Dynamic Computational Graph in PyTorch

## Overview
This project demonstrates how PyTorch dynamically builds computational graphs during forward passes. The model structure changes at runtime, making each iteration potentially unique.

## How It Works
The neural network (`DynamicNet`) contains:
- **fc1 (Linear Layer 1)**: Always used in the forward pass.
- **fc2 (Linear Layer 2)**: Randomly applied in certain iterations.

Each time we run the forward pass, a new computational graph is generated. The visualization captures different structures based on whether `fc2` is used.

## Code Explanation

### 1. Model Definition
```python
class DynamicNet(nn.Module):
    def __init__(self):
        super(DynamicNet, self).__init__()
        self.fc1 = nn.Linear(2, 4)  # First layer (always used)
        self.fc2 = nn.Linear(4, 1)  # Second layer (conditionally used)

    def forward(self, x):
        x = torch.relu(self.fc1(x))  # Always used
        
        # Dynamic behavior: Randomly include the second layer
        if torch.rand(1).item() > 0.5:
            print("Applying extra layer dynamically")
            x = torch.relu(self.fc2(x))
        
        return x
```
- `fc1` is **always applied**.
- `fc2` is **randomly included** in ~50% of cases, making the graph dynamic.

### 2. Generating & Saving Graphs
```python
for i in range(num_graphs):
    x_input = torch.randn(1, 2)  # Random input
    output = model(x_input)
    loss = loss_fn(output, target)
    
    dot = make_dot(loss, params=dict(model.named_parameters()))
    dot.render(f"graphs/dynamic_graph_{i}", format="png")
```
- Runs multiple forward passes.
- Generates and saves a different computational graph in each iteration.

### 3. Visualizing & Comparing Graphs
```python
fig, axes = plt.subplots(1, len(graph_filenames), figsize=(15, 5))
for i, filename in enumerate(graph_filenames):
    img = plt.imread(filename)
    axes[i].imshow(img)
    axes[i].axis("off")
    axes[i].set_title(f"Graph {i+1}")
plt.show()
```
- Loads saved graph images.
- Displays them side by side for easy comparison.

## Expected Output
Each iteration generates a different graph:
1. Some graphs show **only `fc1`** (when `fc2` is skipped).
2. Other graphs show **`fc1` and `fc2`** (when `fc2` is included dynamically).

### Example:
- **Graph 1**: Only `fc1` → `fc2` was skipped.
- **Graph 2**: Both `fc1` and `fc2` → Extra computation applied.

## Conclusion
This experiment showcases PyTorch’s dynamic computation graph updates in action. Each forward pass results in a unique graph, illustrating the flexible nature of PyTorch’s autograd system.

---

