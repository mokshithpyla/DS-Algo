class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def coverPoints(self, A, B):
        max_steps = 0
        for i in range(len(A)-1):
            max_steps += max(abs(A[i]-A[i+1]),abs(B[i]-B[i+1]))
        return max_steps
