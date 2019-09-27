t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    plan = list(map(int, input().split()))
    if -1 not in plan:
        print('YES')
        for each in plan:
            print(each, end=' ')
    else:
        ans = []
        places = set()
        for i in range(1, k+1):
            places.add(i)
        for i in range(n):
            if plan[i] != -1:
                places.remove(plan[i])
        unplanned = plan.count(-1)
        for i in range(n):
            if plan[i] != -1:
                ans[i] = plan[i]
            else:
                for each in places:

                    if ans[i-1] != each and ans[]:
                        ans[i] = each


