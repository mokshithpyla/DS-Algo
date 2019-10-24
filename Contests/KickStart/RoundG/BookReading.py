t = int(input())
for _ in range(t):
    n, m, q = map(int, input().split())
    ans = 0
    torn_out_pages = list(map(int, input().split()))
    r = list(map(int, input().split()))
    pages = [0] * (n+1)
    # for i in range(1, n+1):
    #     pages[i] = 0
    for each in torn_out_pages:
        pages[each] = -1
    for each in r:
        i = 1
        while each*i <= n:
            if pages[each*i] != -1:
                pages[each*i] += 1
            i += 1
    ans = sum(pages) + m
    # for each in torn_out_pages:
    #     for reader in r:
    #         if each % reader == 0:
    #             ans -= 1
    # for each in r:
    #     ans += n//each
    print("Case #{}: {}".format(_+1, ans))



