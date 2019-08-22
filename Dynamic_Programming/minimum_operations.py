t = int(input())
for _ in range(t):
    N = int(input())
    b = bin(N)
    ans = len(b)-2 + b.count('1') - 1
    print(ans)
