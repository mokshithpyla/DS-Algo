class Solution:
    # @param A : list of integers
    # @return an integer
    def maxSpecialProduct(self, nums):
        left = [0]*len(nums)
        right = [0]*len(nums)


        stack = []
        for i in range(len(nums)):
            while len(stack) > 0 and stack[-1][0] < nums[i]:
                curr, idx = stack.pop()
                left[idx] = i
            stack.append((nums[i], i))

        stack = []
        for i in range(len(nums)-1, -1, -1):
            while len(stack) > 0 and stack[-1][0] < nums[i]:
                curr, idx = stack.pop()
                right[idx] = i
            stack.append((nums[i], i))

        res = [0]*len(nums)

        for i in range(len(nums)):
            res[i] = left[i]*right[i]

        return(max(res)%1000000007)
s = Solution()
ans = s.maxSpecialProduct([5, 9, 6, 8, 6, 4, 6, 9, 5, 4, 9])
print(ans)
