class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        A.sort()
        if A[0] > 0:
            if A[0] == len(A) - 1:
                return 1
            else:
                return -1
        else:
            flag = False
            neg = 0
            for i in range(len(A)):
                if A[i] < 0:
                    neg += 1
                else:
                    flag = True
                    break
            if not flag:
                return -1
            zero_count = A.count(0)
            for i in range(neg+zero_count, len(A)):
                sub = A[i+1:]
                if A[i] == len(sub) and A[i] < A[i+1]:
                    return 1
            if zero_count + neg == len(A):
                return 1
            return -1

s = Solution()
ans = s.solve([4, -9, 8, 5, -1, 7, 5, 3])
print(ans)
