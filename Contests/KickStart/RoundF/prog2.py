t = int(input())
for _ in range(t):
    n, s = map(int, input().split())
    skill_set = []
    for i in range(n):
        x = list(map(int, input().split()))
        x.pop(0)
        skill_set.append(set(x))
    ans = 0
    for i in range(n-1):
        for j in range(i+1, n):
            if len(skill_set[i].difference(skill_set[j])) > 0:
                ans += 1
            if len(skill_set[j].difference(skill_set[i])) > 0:
                ans += 1
    print("Case #{}: {}".format(_+1, ans))

