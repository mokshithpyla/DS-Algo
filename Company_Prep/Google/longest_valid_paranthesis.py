'''
Given a string S consisting of opening and closing parenthesis '(' and ')'. Find length of the longest valid parenthesis substring.

Input:
First line contains number of test cases T.  Each test case have one line string S of character '(' and ')' of length  N.

Constraints:
1 <= T <= 500
1 <= N <= 105

Example:
Input:
2
((()
)()())

Output:
2
4

Explanation:
Testcase 1: Longest valid balanced parantheses is () and its length is 2.
'''

#code
t = int(input())
for _ in range(t):
    S = input()
    stack = []
    stack.append(-1)
    ans = 0
    for i in range(len(S)):
        if S[i] == '(':
            stack.append(i)
        else:
            stack.pop()
            if len(stack) != 0:
                ans = max(ans, i - stack[-1])
            else:
                stack.append(i)
    print(ans)
