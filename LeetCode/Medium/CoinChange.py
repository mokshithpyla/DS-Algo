# You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
#
# Example 1:
#
# Input: coins = [1, 2, 5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
# Example 2:
#
# Input: coins = [2], amount = 3
# Output: -1
# Note:
# You may assume that you have an infinite number of each kind of coin.


class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # dp = [float('inf')]*(amount+1)
        # dp[0] = 0
        # for i in range(1, amount+1):
        #     for each in coins:
        #         if each <= i:
        #             dp[i] = min(dp[i], 1 + dp[i-each])
        # print(dp)
        # if dp[-1] == float('inf'):
        #     return -1
        # else:
        #     return (dp[-1])


        # Minimum number of Coins

        def go(coins, rem, count):
            if rem < 0:
                return -1
            if rem == 0:
                return 0
            if rem - 1 in count:
                return count[rem-1]
            min_number = float('inf')
            for coin in coins:
                res = go(coins, rem - coin, count)
                if res >= 0 and res < min_number:
                    min_number = 1 + res
            count[rem - 1] = min_number if min_number != float('inf') else -1
            return count[rem -1]
        count = {}
        visited = {}
        if amount < 1:
            return 0
        else:
            return go(coins, amount, count)
                # or
            #return go(coins, amount, pos)

