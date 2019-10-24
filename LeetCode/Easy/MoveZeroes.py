# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
#
# Example:
#
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Note:
#
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.

#
# class Solution(object):
#     def moveZeroes(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: None Do not return anything, modify nums in-place instead.
#         """
#         non_zero = []
#         for each in nums:
#             if each:
#                 non_zero.append(each)
#         for i in range(len(nums)):
#             if i < len(non_zero):
#                 nums[i] = non_zero[i]
#             else:
#                 nums[i] = 0

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        lastSeenZero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                temp = nums[i]
                nums[i] = nums[lastSeenZero]
                nums[lastSeenZero] = temp
                lastSeenZero += 1