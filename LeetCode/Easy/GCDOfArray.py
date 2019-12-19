# Given two function, one is h(x) which includes the products of all the number in an array A[ ] having size N and another function f(x) which denotes the GCD of all the numbers in an array.Your task is to find the value of  h(x)f(x).
#
# Note: Since the answer can be very large, use modulo 109+7.
#
# Input:
# The first line contains an integer T, the number of test cases. Then T test cases follow. Each test case contains two lines. The first line of each test case contains an integer N denoting the size of the array A. The Next line will contain N-space separated integer values i.e A[i].
#
# Output:
# Print the required answer in a new line
#
# Constraints:
# 1 <= T <= 26
# 1 <= N <= 60
# 1 <= Ai <= 104
#
# Example:
# Input:
# 1
# 2
# 2 4
# Output:
# 64
#
# Explanation:
# Testcase1:Product of the array elements is 8 and GCD of the elements is 2. So 82=64.

#code
def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)
t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    fx = A[0]
    hx = 1
    if 0 in A:
        print(0)
    else:
        for i in range(1, n):
            fx = gcd(fx, A[i])
        for each in A:
            hx *= each
        print((hx**fx)% (10 **9 + 7))