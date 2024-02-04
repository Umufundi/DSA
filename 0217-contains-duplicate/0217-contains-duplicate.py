class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        verify = set()
        
        for i in nums:
            if i in verify:
                return True
            verify.add(i)
        return False
        
        