# Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.
#
# Example 1:
#
# Input: [3,2,1,5,6,4] and k = 2
# Output: 5
# Example 2:
#
# Input: [3,2,3,1,2,4,5,5,6] and k = 4
# Output: 4
# Note:
# You may assume k is always valid, 1 ≤ k ≤ array's length.


class Solution(object):
    def partition(self, nums, l, r):
        pivot = nums[r]
        lo = l
        for k in range(l, r+1):
            if nums[k] < pivot:
                nums[k], nums[lo] = nums[lo], nums[k]
                lo+=1
        nums[lo], nums[r] = nums[r], nums[lo]
        return lo
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        i = 0
        j = n - 1
        pos = self.partition(nums, i, j)
        if pos == n - k:
            return nums[pos]
        elif pos > n - k:
            return self.findKthLargest(nums[:pos], k - (n - pos) )
        else:
            return self.findKthLargest(nums[pos+1:], k)
