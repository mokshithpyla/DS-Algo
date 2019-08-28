t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    sums = [A[i] for i in range(n)]
    for i in range(1, n):
        for j in range(i):
            if A[i] > A[j] and sums[i] < sums[j] + A[i]:
                sums[i] = sums[j] + A[i]
    print(max(sums))