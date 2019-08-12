# cook your dish here
def finalNum(num):
    temp = 0
    placeVal = 1

    for j in range(1,len(num))[::-1]:
        if num[j-1] != num[j]:
            temp += int(num[j])*placeVal
        placeVal *= 10

    temp += int(num[0])*placeVal
    return temp%modu

for _ in range(int(input())):

    nl, l = map(int,input().split())
    nr, r = map(int,input().split())

    modu = 1000000007
    totalSum = 0

    for i in range(l,r+1):
        totalSum = (totalSum + finalNum(str(i)))%modu

    print(totalSum)

# 3
# 1 9
# 2 97
# 1 8
# 2 12
# 1 1
# 1 8