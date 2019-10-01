# You are given coins of different denominations and a total amount of money.
# Write a function to compute the number of combinations that make up that amount.
# You may assume that you have infinite number of each kind of coin.


class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        dp = [0] * (amount + 1)
        dp[0] = 1
        if amount == 0 and not coins:
            return 1
        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] += dp[i-coin]
        return dp[-1]

        # def go(amount, coins, index):
        #     if amount == 0:
        #         return 1
        #     if index >= len(coins):
        #         return 0
        #     if (index, amount) in visited:
        #         return visited[(index, amount)]
        #     repetitions = 0
        #     ways = 0
        #     while coins[index] * repetitions <= amount:
        #         ways += go(amount - coins[index] * repetitions, coins, index + 1)
        #         repetitions += 1
        #     visited[(index, amount)] = ways
        #     return ways
        # visited = {}
        # return go(amount, coins, 0)