# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        
        def inorder(node):
            nonlocal count
            if not node:
                return None
            
            # Traverse left subtree
            left = inorder(node.left)
            if left is not None:
                return left
            
            # Visit current node
            count += 1
            if count == k:
                return node.val
            
            # Traverse right subtree
            return inorder(node.right)
        
        return inorder(root)

        