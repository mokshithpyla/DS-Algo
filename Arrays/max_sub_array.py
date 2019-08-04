class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
        max_sub_array = {}
        max_sum = 0
        j = 0
        for i in range(len(A)):
            if A[i] >= 0:
                max_sum += A[i]
            else:
                max_sub_array[max_sum] = A[j:i]
                max_sum = 0
                j = i+1
        if max_sum not in max_sub_array:
            max_sub_array[max_sum] = A[j:len(A)]
        else:
            op1 = max_sub_array[max_sum]
            op2 = A[j:len(A)]
            if len(op1)>len(op2):
                max_sub_array[max_sum] = op1
            else:
                max_sub_array[max_sum] = op2
        return max_sub_array[max(max_sub_array)]
