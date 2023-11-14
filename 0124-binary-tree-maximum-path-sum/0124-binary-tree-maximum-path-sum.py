# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max_sum = float('-inf')
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if root:
                left = dfs(root.left)
                right = dfs(root.right)
                self.max_sum = max(self.max_sum, root.val, root.val+left, root.val+right, root.val+left+right)
                return max(root.val, root.val+left, root.val+right)
            else:
                return 0
        dfs(root)
        return self.max_sum
            
            