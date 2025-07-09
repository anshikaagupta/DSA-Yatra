# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(node, curr):
            if not node:
                return 0
            curr +=node.val
            count=prefix_sum.get(curr-targetSum, 0)
            prefix_sum[curr]=prefix_sum.get(curr, 0)+1
            count +=dfs(node.left, curr)
            count+=dfs(node.right, curr)
            prefix_sum[curr] -=1
            return count
        prefix_sum={0:1}
        return dfs(root, 0)
        