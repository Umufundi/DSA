class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i = 0

        # Iterate through the elements in nums
        while i < len(nums) and nums[i] < target:
            i += 1

        return i