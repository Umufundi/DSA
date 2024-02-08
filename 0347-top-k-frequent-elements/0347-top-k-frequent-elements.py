
'''
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
 

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.


'''

'''

from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        occurence = Counter(nums)  
        ans = []
        
        for num, _ in occurence.most_common(k):  
            ans.append(num)
            
        return ans

   

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

        # O(n)
'''

from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count the frequency of each element in nums
        frequency_map = Counter(nums)
        
        # Step 2: Create buckets to store elements based on their frequency
        max_frequency = max(frequency_map.values())
        buckets = [[] for _ in range(max_frequency + 1)]
        for num, freq in frequency_map.items():
            buckets[freq].append(num)
        
        # Step 3: Retrieve the top k frequent elements from the buckets
        result = []
        for bucket in reversed(buckets):
            result.extend(bucket)
            if len(result) >= k:
                break
        
        return result[:k]
