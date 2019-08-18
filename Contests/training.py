t = int(input())
for _ in range(t):
    n, p = map(int, input().split())
    skill_rating = list(map(int, input().split()))
    skill_rating.sort(reverse=True)
    # print('test', _)
    sums = [0]*n
    sums[0] = skill_rating[0]
    for i in range(1, n):
        sums[i] = sums[i-1] + skill_rating[i]
    min_diff = abs(skill_rating[0]*p - sums[p-1])
    for i in range(1, n-p+1):
        diff = abs(skill_rating[i]*p - abs(sums[i+p-1] - sums[i-1]))
        min_diff = min(diff, min_diff)
    # print('Case #%d: %d' % (_+1, min_diff))
    print("Case #{}: {}".format(_+1, min_diff))



