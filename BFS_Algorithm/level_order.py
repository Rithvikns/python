from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def level_order(root):
  if not root:
    return []
  queue = deque([root])
  result = []

  while queue:
    level = []
    for _ in range(len(queue)):
      node = queue.popleft()
      level.append(node.val)
      if node.left:
        queue.append(node.left)
      if node.right:
        queue.append(node.right)
    result.append(level)
  return result

def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)
    print(level_order(root))

if __name__ == "__main__":
   main()
