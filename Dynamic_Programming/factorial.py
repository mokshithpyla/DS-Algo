def fact(N):
    if N in memo:
        print('memoized')
        return memo[N]

    if N is 1 or N is 0:
        return 1
    else:
        f = N * fact(N-1)
    memo[N] = f
    return f
memo = {}
print(fact(5))
print(memo)
print(fact(10000))
print(memo)