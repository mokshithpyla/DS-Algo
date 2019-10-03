# Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
#
# Your algorithm's runtime complexity must be in the order of O(log n).
#
# If the target is not found in the array, return [-1, -1].
#
# Example 1:
#
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:
#
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def binarySearch(left, right, target, hasOccured):
            if left > right:
                return -1
            mid = left + (right - left) // 2
            if nums[mid] == target:
                if not hasOccured:
                    if mid - 1 >= 0 and nums[mid-1] == nums[mid]:
                        return binarySearch(left, mid - 1, target, hasOccured)
                else:
                    if mid + 1 <= len(nums) - 1 and nums[mid+1] == nums[mid]:
                        return binarySearch(mid + 1, right, target, hasOccured)
                return mid
            elif target > nums[mid]:
                return binarySearch(mid + 1, right, target, hasOccured)
            else:
                return binarySearch(left, mid - 1, target, hasOccured)
        first = binarySearch(0, len(nums)-1, target, False)
        if first != -1:
            last = binarySearch(0, len(nums)-1, target, True)
            return [first, last]
        else:
            return [-1, -1]