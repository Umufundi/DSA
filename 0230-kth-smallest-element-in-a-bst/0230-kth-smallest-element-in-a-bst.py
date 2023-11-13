# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import heapq
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.result = None
        
        def helper(root):
            if not root or self.k == 0:
                return
            
            helper(root.left)
            self.k -=1
            if self.k == 0:
                self.result = root.val
            helper(root.right)
        helper(root)
        
        return self.result
            
            
        