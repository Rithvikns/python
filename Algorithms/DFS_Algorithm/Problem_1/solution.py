class Node:
    def __init__(self, val, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

def flatten(head):
    if not head:
        return None

    stack = []
    current = head

    while current:
        if current.child:
            if current.next:
                stack.append(current.next)  # Store the next node

            current.next = current.child
            current.next.prev = current
            current.child = None  # Remove the child pointer

        if not current.next and stack:
            next_node = stack.pop()
            current.next = next_node
            next_node.prev = current

        current = current.next

    return head
