# Given a non-empty array of integers, return the k most frequent elements.
#
# Example 1:
#
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:
#
# Input: nums = [1], k = 1
# Output: [1]
# Note:
#
# You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
# Your algorithm's time complexity must be better than O(n log n), where n is the array's size.


from collections import Counter
from heapq import heapify , heappush , heappop

class Solution(object):
    def topKFrequent(self, nums, k):
        queue = []
        count = Counter(nums)
        for num , freq in count.items():
            heappush(queue , (freq , num))
            if len(queue) > k:
                heappop(queue)
        return [ num for freq , num in queue]
