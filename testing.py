# def alter(serve):
#     if serve=='Chef':
#         return 'Paja'
#     else:
#         return 'Chef'
# t=int(input())
# for _ in range(t):
#     x,y,k=map(int,input().split())
#     games=x+y
#     serve='Chef'
#     changes=games//k
#     if changes%2==0:
#         print('Chef')
#     else:
#         print('Paja')
#
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

# t=int(input())
# for _ in range(t):
#     n,d=map(int,input().split())
#     p=list(map(int,input().split()))
#     original_p=p[:]
#     p.sort()
#     count=0
#     for i in range(n):
#         if abs(p[i]-original_p[i])==d:
#             count+=1
#     if count==0:
#         print("-1")
#     else:
#         print(count//2+1)
