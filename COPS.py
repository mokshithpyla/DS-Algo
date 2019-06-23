# https://www.codechef.com/submit/COPS

t=int(input())
for _ in range(t):
    M,x,y=map(int,input().split())
    cop_power=x*y
    cop_houses=list(map(int,input().split()))
    houses=[1]*101
    houses[0]=0
    for each in cop_houses:
        start=each-cop_power
        end=each+cop_power
        if start<0:
            start=1
        if end>100:
            end=100
        houses[start:end+1]=[0]*(end-start)
    safe=houses.count(1)
    print(safe)

# 3
# 4 7 8
# 12 52 56 8
# 2 10 2
# 21 75
# 2 5 8
# 10 51