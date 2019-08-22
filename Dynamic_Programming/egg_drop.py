def egg_drop(n, k):
    trials = [[0 for x in range(k+1)] for x in range(n+1)]
    for i in range(1, n+1):
        trials[i][1] = 1
        trials[i][0] = 0
    for j in range(1, k+1):
        trials[1][j] = j
    for i in range(2, n+1):
        for j in range(2, k+1):
            trials[i][j] = INT_MAX
            for x in range(1, j+1):
                res = 1 + max(trials[i-1][x-1], trials[i][j-x])
                if res < trials[i][j]:
                    trials[i][j] = res
    return trials[n][k]
INT_MAX = 32678
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    print(egg_drop(n, k))

# 2
# 2 10
# 3 5