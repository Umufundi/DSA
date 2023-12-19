class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        
        majority = len(nums)//2
        
        track ={}
        for i in nums:
            if i in track:
                track[i] +=1
            else:
                track[i] = 1
        maj = max(track, key = track.get)
        
        return maj
    
    
'''
from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        majority_element = max(count, key=count.get)
        return majority_element

'''
        