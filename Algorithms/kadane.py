def kadane(A):
    global_max = curr_max = A[0]
    for i in range(1, len(A)):
        curr_max = max(A[i], curr_max+A[i])
        global_max = max(curr_max, global_max)
    return global_max


print(kadane([-2, 3, 2, -1]))
