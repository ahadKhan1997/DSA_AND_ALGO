from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder_traversal(root):
    if root is None:
        return
    
    inorder_traversal(root.left)   # Visit Left
    print(root.val, end=" ")       # Process Root
    inorder_traversal(root.right)  # Visit Right

def preorder_traversal(root):
    if root is None:
        return
    print(root.val, end=" ")
    preorder_traversal(root.left)
    preorder_traversal(root.right)

def postorder_traversal(root):
    if root is None:
        return
    postorder_traversal(root.left)
    postorder_traversal(root.right)
    print(root.val, end=" ")

def level_order_traversal(root):
    if not root:
        return []
    
    queue = deque([root])
    result = []
    
    while queue:
        node = queue.popleft()     # Remove from front of queue
        result.append(node.val)
        
        if node.left:
            queue.append(node.left)   # Add left child to back
        if node.right:
            queue.append(node.right)  # Add right child to back
            
    return result

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)

print("------------------ DEPTH FIRST SEARCH ----------------------------------")
print("Inorder Traversal: ")
inorder_traversal(root)
print("\nPreorder Traversal: ")
preorder_traversal(root)
print("\nPostorder Traversal: ")
postorder_traversal(root)

print("------------------ BREADTH FIRST SEARCH ----------------------------------")

BFS = level_order_traversal(root)
print(BFS)
