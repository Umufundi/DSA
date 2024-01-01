class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
            nums1.append(nums2[i])
            if 0 in nums1:
                nums1.remove(0)
        nums1.sort()