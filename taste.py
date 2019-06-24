t=int(input())
for _ in range(t):
    n,d=map(int,input().split())
    day_and_taste={}
    days=[]
    for i in range(n):
        x,y=map(int,input().split())
        if x not in days:
            days.append(x)
            day_and_taste[x]=y
        else:
            if y>day_and_taste[x]:
                day_and_taste[x]=y
    tastes=list(day_and_taste.values())
    tastiness=0
    tastiness+= max(tastes)
    tastes.remove(max(tastes))
    tastiness+=max(tastes)
    # tastes.sort()
    # tastiness=tastes[-1]+tastes[-2]
    print(tastiness)
    # tastiness=0
    # for i in range(n):
    #

    # print(tastiness)

#     3 7
# 5 12
# 2 5
# 5 10

# 2
# 3 6
# 5 7
# 1 9
# 2 5
# 3 7
# 5 8
# 2 5
# 5 10