# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque 
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return None
        
        queue = deque()
        queue.append(root)
        result =[]
        
        while queue:
            level_node = []
            lenght = len(queue)
            
            for _ in range(lenght):
                node = queue.popleft()
                level_node.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level_node)
            
        return reversed(result)
                
        
        