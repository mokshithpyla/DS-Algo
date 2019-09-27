# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
#
# Note:
#
# The number of elements initialized in nums1 and nums2 are m and n respectively.
# You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
# Example:
#
# Input:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
#
# Output: [1,2,2,3,5,6]


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        nums1 = nums1[:len(nums1)-len(nums2)]
        nums3 = [None]*(len(nums1)+len(nums2))
        k = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                nums3[k] = nums1[i]
                k += 1
                i += 1
            else:
                nums3[k] = nums2[j]
                j += 1
                k += 1
        while i< len(nums1)-len(nums2):
            nums3[k] = nums1[i]
            k = k + 1
            i = i + 1
        while j < len(nums2):
            nums3[k] = nums2[j]
            k = k + 1
            j = j + 1
        print(nums3)
        nums1 = nums3[:]
