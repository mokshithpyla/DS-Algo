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


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # push over elements in nums1
        idx = len(nums1) - 1
        i = m - 1
        while i >= 0:
            nums1[idx] = nums1[i]
            i = i - 1
            idx = idx - 1

        # merge
        j = 0
        i = n
        k = 0
        while i < (m + n) and j < n:
            if nums1[i] < nums2[j]:
                nums1[k] = nums1[i]
                i = i + 1
            else:
                nums1[k] = nums2[j]
                j = j + 1
            k = k + 1

        # copy over any remaining elements from nums2
        if j < n:
            k = n - 1
            l = m + n - 1
            while k >= j:
                nums1[l] = nums2[k]
                k = k - 1
                l = l - 1