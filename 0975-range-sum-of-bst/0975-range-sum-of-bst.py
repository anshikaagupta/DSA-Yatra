# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        sum=0
        def inorder(root, low, high):
            nonlocal sum
            if root:
                inorder(root.left, low, high)
                if root.val>=low and root.val<=high:
                    sum +=root.val
                inorder(root.right, low, high)
        inorder(root, low, high)
        return sum
        