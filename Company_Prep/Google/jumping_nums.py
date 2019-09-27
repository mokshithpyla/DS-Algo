'''
Given a positive number X. Find all Jumping Numbers smaller than or equal to X.
Jumping Number: A number is called Jumping Number if all adjacent digits in it differ by only 1. All single digit numbers are considered as Jumping Numbers. For example 7, 8987 and 4343456 are Jumping numbers but 796 and 89098 are not.

Input:
The first line of the input contains T denoting the number of testcases. Each testcase contain a positive number X.

Output:
Output all the jumping numbers less than X in sorted order. Jump to example for better understanding.

Constraints:
1 <= T <= 100
1 <= N <= 109

Example:
Input:
2
10
50
Output:
0 1 2 3 4 5 6 7 8 9 10
0 1 2 3 4 5 6 7 8 9 10 12 21 23 32 34 43 45

Explanation:
Testcase 2: Here, the most significant digits of each jumping number is following increasing order, i.e., jumping numbers starting from 0, followed by 1, then 2 and so on, themselves being in increasing order 2, 21, 23.
'''


def bfs(x, num):
    q = []
    q.append(num)
    while len(q) != 0:
        num = q.pop(0)
        if num <= x:
            ans.append(num)
            ld = num % 10
            if ld == 0:
                q.append(num*10 + ld + 1)
            elif ld == 9:
                q.append(num*10 + ld - 1)
            else:
                q.append(num*10 + ld - 1)
                q.append(num*10 + ld + 1)


t = int(input())
for _ in range(t):
    x = int(input())
    print('0', end=' ')
    ans = []
    for i in range(1, 10):
        bfs(x, i)
    ans.sort()
    for each in ans:
        print(each, end=' ')
    print()

