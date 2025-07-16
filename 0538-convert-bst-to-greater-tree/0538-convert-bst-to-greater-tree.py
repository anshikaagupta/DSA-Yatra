# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        curSum=0
        fullSum=0
        def findSum(root):
            nonlocal fullSum
            if root:
                fullSum +=root.val
                findSum(root.left)
                findSum(root.right)

        def inorder(root):
            nonlocal fullSum
            nonlocal curSum
            if root:
                inorder(root.left)
                curSum +=root.val
                root.val +=fullSum -curSum
                inorder(root.right)
        findSum(root)
        inorder(root)
        return root
        