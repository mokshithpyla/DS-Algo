# https://www.codechef.com/problems/SILLYPRS

t=int(input())
while(t):
    t=t-1
    n=int(input())
    lia=list(map(int,input().split()))
    lib=list(map(int,input().split()))
    odda=0
    oddb=0
    for i in lia:
        if(i%2==1):
            odda+=1;
    for i in lib:
        if(i%2==1):
            oddb+=1;
    x=abs(odda-oddb)
    y=sum(lia)+sum(lib)-x
    print(y//2)
