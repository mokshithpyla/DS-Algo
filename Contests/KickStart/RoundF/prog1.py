t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    k1 = 0
    stack = []
    solved = False
    for i in range(n):
        if i < n - 1:
            if A[i] != A[i+1]:
                k1 += 1
        if stack and stack[-1][0] == A[i]:
            stack[-1][1] += 1
        else:
            stack.append([A[i], 1])
    if k1 <= k:
        changes = 0
    else:
        changes = 0
        for i in range(1, n-2):
            if k1 <= k:
                solved = True
                break
            if stack[i-1][0] != stack[i][0] and stack[i][0] != stack[i+1][0]:
                if stack[i-1][0] == stack[i+1][0]:
                    stack[i][0] = stack[i+1][0]
                    changes += stack[i][1]
                    k1 -= 2
        if not solved:
            for i in range(1, n-2):
                if k1 <= k:
                    solved = True
                    break
                if stack[i-1][0] != stack[i][0] and stack[i][0] != stack[i+1][0]:
                    m = min(stack[i-1][1], stack[i][1], stack[i+1][1])
                    if stack[i-1][1] == m:
                        stack[i-1][0] = stack[i][0]
                    elif stack[i][1] == m:
                        stack[i][0] = stack[i+1][0]
                    else:
                        stack[i+1][0] = stack[i][0]
                    changes += m
                    k1 -= 1
    print("Case #{}: {}".format(_+1, changes))
