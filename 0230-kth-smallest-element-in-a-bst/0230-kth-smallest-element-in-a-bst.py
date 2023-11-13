# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import heapq
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        heap =[]
        
        def helper(root):
            if not root:
                return
            heapq.heappush(heap,root.val)
            helper(root.left)
            helper(root.right)
        helper(root)
        for _ in range(k-1):
            heapq.heappop(heap)
        return heapq.heappop(heap)
            
            
        