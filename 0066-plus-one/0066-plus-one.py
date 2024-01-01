class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        """
        add list component to string 
        convert string to integer
        integer +1
        make the integer a list and return
        
        
        or 
        
        
        at digit[-1] +1
        if len(value) == 2
            value = digit[-1-1] +1
        
        """
        
        if digits[-1] == 9:
            if len(digits) == 1:  # Already a 9
                return [1, 0]
            return self.plusOne(digits[:-1]) + [0]
        else:
            digits[-1] += 1
        return digits
        