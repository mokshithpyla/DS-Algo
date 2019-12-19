

n,u,d=map(int,input().split())
a=[int(i) for i in input().split()]
idx=0
i=0
while(i<n-1):
    if(a[i+1]-a[i]<=u and a[i+1]+d>=a[i]):
        i=i+1
        continue
    elif(a[i+1]<a[i]):
        i=i+1

    else:
        break
print(i+1, end="")