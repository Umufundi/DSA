# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        result = [root.val]
        
     
        right_result = self.rightSideView(root.right)
        left_result = self.rightSideView(root.left)
        
   
        result.extend(right_result)
        
        
        if len(left_result) > len(right_result):
            result.extend(left_result[len(right_result):])
        
        return result
        