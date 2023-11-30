class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        # List of open and closed parentheses
        open_p = ['(', '[', '{']
        closed_p = [')', ']', '}']
        
        for i in s:
            if i in open_p:
                stack.append(i)
            elif i in closed_p:
                # Check if the stack is empty before accessing the last element
                if not stack or closed_p.index(i) != open_p.index(stack[-1]):
                    return False
                stack.pop()
        
        return not stack
