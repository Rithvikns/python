from collections import defaultdict

class Tree:
    def __init__(self, edges):
        self.tree = defaultdict(list)
        self.nodes = set()
        self.children = set()
        
        # Build adjacency list representation of the tree
        for parent, child, weight in edges:
            self.tree[parent].append((child, weight))
            self.nodes.add(parent)
            self.nodes.add(child)
            self.children.add(child)
        
        # Find the root (a node that is never a child)
        self.root = list(self.nodes - self.children)[0]

    def max_sum_path(self):
        """Finds the maximum sum from root to leaf using DFS."""
        def dfs(node):
            if node not in self.tree:  # Leaf node
                return 0
            
            max_sum = float('-inf')
            for child, weight in self.tree[node]:
                max_sum = max(max_sum, weight + dfs(child))
            
            return max_sum
        
        return dfs(self.root)

# Example usage
edges = [
    (1, 2, 3),
    (1, 3, 5),
    (2, 4, 7),
    (2, 5, 6),
    (3, 6, 4),
    (3, 7, 8)
]

tree = Tree(edges)
print("Maximum sum from root to leaf:", tree.max_sum_path())

