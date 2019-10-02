# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
#
# Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.
#
# Example 1:
#
# Input: [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.
# Example 2:
#
# Input: [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
# Total amount you can rob = 2 + 9 + 1 = 12.

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #         if nums:
        #             if len(nums)==1:
        #                 return nums[0]
        #             # dp = [0]*len(nums)
        #             # dp[0] = nums[0]
        #             pre = nums[0]
        #             curr = max(nums[0],nums[1])
        #             # dp[1] = max(nums[0],nums[1])
        #             for i in range(2, len(nums)):
        #                 # dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        #                 curr, pre = max(pre+nums[i], curr), curr
        #             return curr
        #         else:
        #             return 0

        # Recursive :

        def go(index):
            if index >= len(nums):
                return 0
            elif index in visited:
                return visited[index]
            else:
                max_money = max(go(index+1), nums[index] + go(index + 2))
                visited[index] = max_money
                return visited[index]
        index = 0
        visited = {}
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        else:
            return go(index)