class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # Approach 1: DP
        # dp = [0]*len(s)
        # longestValid = 0
        # for i in range(len(s)):
        #     if s[i] == '(':
        #         dp[i] = 0
        #     else:
        #         if i == 0:
        #             continue
        #         if s[i - 1] == '(':
        #             dp[i] = dp[i - 2] + 2
        #         else:
        #             if i - dp[i - 1] - 1 < 0:
        #                 continue
        #             if s[i - dp[i - 1] - 1] == '(':
        #                 dp[i] = dp[i - 1] + dp[i - dp[i-1] - 2] + 2
        #     longestValid = max(longestValid, dp[i])
        # return longestValid
        # Approach 2: Efficient two pointer
        left = 0
        right = 0
        longestValid = 0
        for each in s:
            if each == '(':
                left += 1
            else:
                right += 1
            if left == right:
                longestValid = max(longestValid, 2 * right)
            elif right > left:
                left = right = 0
        left = right = 0
        for each in s[::-1]:
            if each == '(':
                left += 1
            else:
                right += 1
            if left == right:
                longestValid = max(longestValid, 2 * left)
            elif left > right:
                left = right = 0
        return longestValid
            