def findNextGreatest(rest,ele):
    rest.sort()
    return rest[rest.index(ele)+1]
num=input()
n=[]
for digit in num:
    n.append (int(digit))
for i in range(len(n)-2,0,-1):
    if n[i]<n[i+1]:
        # nextg=n.index(min(n[i+1:]))
        nextg=findNextGreatest(n[i:],n[i])
        blah=n.index(nextg)
        t=n[i]
        n[i]=n[blah]
        n[blah]=t
        k=n[i+1:]
        k.sort()
        n=n[:i+1]
        n.extend(k)
        break
print(n)


# 1 5 4 8 3
# 8 5 4 3 1
# 1 4 7 4 5 8 4 1 2 6