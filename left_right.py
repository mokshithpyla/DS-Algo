def maxSpecialProduct(A):
    special_value = 0
    for i in range(1, len(A)-1):
        LeftSpecialValue = 0
        RightSpecialValue = len(A) - 1
        special_value =0
        for j in range(i):
            if A[j] > A[i]:
                LeftSpecialValue = max(j, LeftSpecialValue)
        found = False
        for j in range(i+1, len(A)):
            if A[j] > A[i]:
                found = True
                RightSpecialValue = min(j, RightSpecialValue)
        if not found:
            RightSpecialValue = 0
        special_value = max(special_value, LeftSpecialValue*RightSpecialValue)
    return special_value

maxSpecialProduct([ 5, 9, 6, 8, 6, 4, 6, 9, 5, 4, 9 ])