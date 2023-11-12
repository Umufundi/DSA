class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return []
        dictionary = {}
        for i, num in enumerate(nums):
            if target - num in dictionary:
                return [dictionary[target-num], i]
            dictionary[num] = i
        return []