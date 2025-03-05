# Graph Neural Network (GNN) with PyTorch Geometric and Visualization

This repository demonstrates the implementation of a **simple Graph Neural Network (GNN)** using **PyTorch Geometric** for graph data processing, along with a visualization of the graph structure using **NetworkX** and **Matplotlib**.

## 📄 Overview

The goal of this script is to:
1. Create a graph representation using PyTorch Geometric, with nodes, edges, and edge weights.
2. Build a simple **Graph Convolutional Network (GCN)** for node feature transformation.
3. Perform a forward pass through the GNN to get the node feature outputs.
4. Visualize the graph using **NetworkX** and **Matplotlib**.

---

## 🛠️ Installation

Before running the script, ensure the following dependencies are installed:

```bash
pip install torch torch_geometric networkx matplotlib numpy
'''

PyTorch: The deep learning framework used to build and train neural networks.
PyTorch Geometric: A library built on top of PyTorch to handle graph data and implement graph neural networks (GNNs).
NetworkX: A package for the creation, manipulation, and study of the structure, dynamics, and functions of complex networks.
Matplotlib: A plotting library used for graph visualization.

📂 Files
gnn_pytorch.py
This Python script demonstrates the entire process of creating a simple graph, defining a GNN, performing a forward pass, and visualizing the results.

## 🖥️ Code Explanation
1. Graph Data (Edges and Weights)
We define the graph with nodes, edges, and edge weights.

Edges are represented as pairs of node indices (source, target).
Weights are associated with the edges to signify the strength of connections.
python
Copy
Edit
edges = torch.tensor([[0, 1, 2, 3], [1, 2, 3, 0]], dtype=torch.long)  # (source, target)
weights = torch.tensor([0.5, 0.8, 0.6, 0.9], dtype=torch.float)  # Edge weights
edges: A tensor representing the source and target nodes of the edges in the graph.
weights: A tensor representing the weights of each edge.
2. Node Features
In this example, we generate random node features (3-dimensional) for each node. These node features could represent attributes like node degree, centrality, or any other property relevant to the problem.

python
Copy
Edit
node_features = torch.rand((num_nodes, 3))
node_features: A tensor with shape (num_nodes, num_features). Here, num_nodes=4 and each node has 3 random features.
3. PyTorch Geometric Data Object
Next, we combine the graph's nodes, edges, and weights into a PyTorch Geometric Data object.

python
Copy
Edit
graph_data = Data(x=node_features, edge_index=edges, edge_attr=weights)
x: Node features.
edge_index: List of edges (source, target).
edge_attr: Edge attributes (weights).
4. Graph Neural Network Model
We define a simple Graph Convolutional Network (GCN) model using two graph convolutional layers (GCNConv).

python
Copy
Edit
class SimpleGNN(torch.nn.Module):
    def __init__(self):
        super(SimpleGNN, self).__init__()
        self.conv1 = GCNConv(3, 16)  # Input: 3 features, Output: 16 features
        self.conv2 = GCNConv(16, 2)  # Output: 2 features (for example, binary classification)

    def forward(self, data):
        x, edge_index = data.x, data.edge_index
        x = self.conv1(x, edge_index)
        x = F.relu(x)
        x = self.conv2(x, edge_index)
        return x
GCNConv(3, 16): The first layer transforms the node features from 3 to 16 dimensions.
GCNConv(16, 2): The second layer reduces the node features from 16 to 2 dimensions (for binary classification, for example).
ReLU Activation is applied between the layers.
5. Forward Pass and Output
We perform a forward pass through the model to get the transformed node features.

python
Copy
Edit
model = SimpleGNN()
output = model(graph_data)
The output contains the final node features after passing through the GCN layers.
6. Graph Visualization
We use NetworkX to visualize the graph and Matplotlib to display it.

python
Copy
Edit
G = nx.DiGraph()
for i in range(edges.shape[1]):
    G.add_edge(int(edges[0, i]), int(edges[1, i]), weight=weights[i].item())

plt.figure(figsize=(5, 5))
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=12)
nx.draw_networkx_edge_labels(G, pos, edge_labels={(int(edges[0, i]), int(edges[1, i])): f'{weights[i]:.2f}' for i in range(edges.shape[1])})
plt.title("Graph Representation of Structured Data")
plt.show()
NetworkX creates the graph and Matplotlib handles the visualization.
Each edge is annotated with its corresponding weight.
🧠 Model Forward Pass and Visualization Output
Node Features Output: After performing a forward pass through the GCN, you will see the updated node features (a tensor with shape (num_nodes, 2)).

Graph Visualization: A plot showing the graph structure with nodes, edges, and edge weights.

📌 Conclusion
This simple script demonstrates how to:

Build a graph in PyTorch Geometric.
Define a basic Graph Convolutional Network model.
Perform a forward pass to get node representations.
Visualize the graph using NetworkX and Matplotlib.
You can extend this to implement more complex GNN architectures like Graph Attention Networks (GAT) or GraphSAGE, and work with larger datasets.

🤝 Contributing
Feel free to submit pull requests or raise issues to enhance the functionality of the repository. Contributions are welcome!

👨‍💻 Author
This project was created by [Your Name].
