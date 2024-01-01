class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()

        result = []
        i, j = 0, 0

        # Iterate through both arrays
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                # Append the common element to the result
                result.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1

        return result
        