# https://www.codechef.com/submit/SALARY
# Hint: Increasing salary of only winners is same as decreasing for just the loser
t=int(input())
for _ in range(t):
    n=int(input())
    s=list(map(int,input().split()))
    turns = 0
    s.sort()
    print(s)
    for i in range(n):
        turns+=s[i]-s[0]
    print(turns)