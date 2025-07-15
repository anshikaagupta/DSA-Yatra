# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        x=None
        y=None
        prev=None
        def inorder(root):
            nonlocal x
            nonlocal y
            nonlocal prev
            if root:
                inorder(root.left)
                if x is None:
                    if prev and prev.val>root.val:
                        x=prev
                        y=root
                else:
                    if prev and prev.val>root.val:
                        y=root
                prev=root
                inorder(root.right)
        inorder(root)
        x.val, y.val=y.val,x.val
        return root
            