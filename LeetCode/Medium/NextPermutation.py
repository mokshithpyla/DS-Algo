# https://practice.geeksforgeeks.org/problems/next-permutation/0

# Implement the next permutation, which rearranges numbers into the numerically next greater permutation of numbers. If such arrangement is not possible, it must be rearranged as the lowest possible order ie, sorted in an ascending order.
#
# For example:
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
#
# Input:
# The first line contains an integer T, depicting total number of test cases. Then following T lines contains an integer N depicting the size of array and next line followed by the value of array.
#
# Output:
# Print the array of next permutation in a separate line.
#
# Constraints:
# 1 ≤ T ≤ 40
# 1 ≤ N ≤ 100
# 0 ≤ A[i] ≤ 100
#
# Example:
# Input:
# 1
# 6
# 1 2 3 6 5 4
#
# Output:
# 1 2 4 3 5 6

#code
t = int(input())
for _ in range(t):
    n = int(input())
    digits = list(map(int, input().split()))
    for i in range(n-1, 0, -1):
        if digits[i] > digits[i-1]:
            break
    smallest = i
    x = digits[i-1]
    for j in range(i-1, n):
        if digits[j] > x and digits[j] < digits[smallest]:
            smallest = j
    digits[i-1], digits[smallest] = digits[smallest], digits[i-1]

    ans = digits[:i] + sorted(digits[i:])
    for each in ans:
        print(each, end=" ")
    print()