# BFS ( Breadth first search) 
It is a traversal algorithm , which means you visit all the nodes in the current depth level and then move to the next level.

1) When you encounter any BFS problem you have to use a queue , queue is used to manage the nodes that are to be visited.
2) start the proccess by enquiring the root node.
3) while queue is not empty then deque a node, process the dequed node and enque its left and right children.
4) Repeat until all nodes are processed.

## BFS is ideal when

1) you need to process the nodes level by level
2) you're solving problems involving proximity ( shortest path)
3) you want to calculate properties of node at same depth.

### Examples

1) Graph Traversal
2) Shortest Path in an Unweighted Graph
3) Word Ladder (String Transformation)
4) Maze Solving (Grid-Based Shortest Path)
5) Connected Components Detection
