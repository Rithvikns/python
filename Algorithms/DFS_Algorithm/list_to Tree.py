from collections import deque

Class TreeNode():
  def __init__(self,val=0,left=None,right=None):
    self.val = val
    self.left = left
    self.right = right

def list_to_tree(lst):
  if not lst:
    return None
  root = TreeNode(lst[0])
  queue = deque(root)
  i = 1
  while i<len(lst):
    current = queue.popleft()
    if lst[i] is not None:
      current.left = TreeNode(lst[i])
      queue.append(current.left)
      i += 1
    if i<len(lst) and lst[i] is not None:
      current.right = TreeNode(lst[i])
      queue.append(current.right)
      i += 1
  return root
      
    
