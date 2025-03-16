# Tree Data Structure

## Overview
A **tree** is a hierarchical data structure that consists of nodes connected by edges. It is widely used in computer science for representing hierarchical relationships, such as file systems, organization charts, and search trees.

## Key Features
- **Root Node**: The topmost node in the tree.
- **Parent-Child Relationship**: Each node (except the root) has one parent and may have multiple children.
- **Leaf Node**: A node with no children.
- **Edge**: A connection between two nodes.
- **Depth**: The number of edges from the root to a node.
- **Height**: The longest path from the root to a leaf node.
- **Subtree**: A tree formed by any node and its descendants.

## Types of Trees
### 1. **Binary Tree**
A tree where each node has at most two children.
- **Full Binary Tree**: Every node has either 0 or 2 children.
- **Complete Binary Tree**: All levels are fully filled except possibly the last, which is filled from left to right.
- **Perfect Binary Tree**: All internal nodes have exactly two children, and all leaf nodes are at the same level.

### 2. **Binary Search Tree (BST)**
A binary tree where:
- The left child contains values less than the parent.
- The right child contains values greater than the parent.
- Enables efficient searching, insertion, and deletion (`O(log N)`).

### 3. **Balanced Trees**
Trees that maintain a balanced height for optimized performance.
- **AVL Tree**: Ensures height balance using rotations.
- **Red-Black Tree**: Maintains balance with color properties.

### 4. **Trie (Prefix Tree)**
A tree used for storing strings efficiently, commonly used in autocomplete and dictionary applications.

### 5. **Heap (Priority Queue)**
A binary tree used for priority-based processing.
- **Min-Heap**: The parent is smaller than its children.
- **Max-Heap**: The parent is larger than its children.

## Applications of Trees
- **File Systems**: Directory structure representation.
- **Databases**: Indexing using B-Trees.
- **AI & Machine Learning**: Decision trees for classification.
- **Compilers**: Abstract syntax trees for parsing code.
- **Networking**: Routing tables and hierarchical addressing.

## Conclusion
Trees are fundamental data structures in computing, providing efficient ways to organize and process hierarchical data. They are essential in various domains, from search optimization to AI and beyond.


