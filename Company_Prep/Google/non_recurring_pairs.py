'''
You are given an array A containing 2*N+2 positive numbers, out of which 2*N numbers exist in pairs whereas the other two number occur exactly once and are distinct. You need to find the other two numbers and print them in ascending order.


Input :
The first line contains a value T, which denotes the number of test cases. Then T test cases follow .The first line of each test case contains a value N. The next line contains 2*N+2 space separated integers.

Output :
Print in a new line the two numbers in ascending order.

Constraints :
1<=T<=100
1<=N<=10^6
1<=A[i]<=5*10^8

Example:
Input :
2
2
1 2 3 2 1 4
1
2 1 3 2

Output :
3 4
1 3
'''

#code
t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    cnt = {}
    for each in nums:
        if each not in cnt:
            cnt[each] = 1
        else:
            cnt[each] += 1
    ans = []
    for each in cnt:
        if cnt[each] % 2 != 0:
            ans.append(each)
    ans.sort()
    for each in ans:
        print(each, end=' ')
    print()