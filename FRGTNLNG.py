# cook your dish here
# https://www.codechef.com/submit/FRGTNLNG
t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    dictionary=input().split()
    phrases=[]
    for each in range(k):
        phrases.append(input().split())
    for each in dictionary:
        flag=False
        for phrase in phrases:
            i=1
            if each in phrase:
                flag=True
                break
        if flag==True:
            print('YES',end=' ')
        else:
            print('NO', end=' ')





# 2
# 3 2
# piygu ezyfo rzotm
# 1 piygu
# 6 tefwz tefwz piygu ezyfo tefwz piygu
# 4 1
# kssdy tjzhy ljzym kegqz
# 4 kegqz kegqz kegqz vxvyj

