# There are N ticket sellers each of whom has a certain amount of tickets. The price of a ticket is the number of tickets remaining with the ticket seller. They can sell a total of K tickets. Find the maximum amount they can earn by selling K tickets.
#
# Input:
# The first line of the input consists of a single integer T denoting the number of test cases. Each of the test case consists of two lines. First line of each test case consists of two integers N and K. The next line contains space separated N integers A[0], A[1], …, A[N-1] where A[i] denotes the number of ticket with ith ticket seller.
#
# Output:
# For each test case, print in a new line, the maximum amount they can earn by selling K tickets. Print your answer modulo 109 + 7​
#
# Constraints:
# 1 <= T <= 103
# 1 <= N <= 105
# 1 <= Ai, K <= 106
#
# Example:
# Input:
# 2
# 5 3
# 4 3 6 2 4
# 6 2
# 5 3 5 2 4 4
# Output:
# 15
# 10
#
# Explanation:
# Assume 0-based indexing
# Testcase 1:
# Firstly, 2nd ticket seller can sell his one ticket at price = 6. Then, he will have 5 tickets with price = 5. He can again sell one ticket with price = 5. Now, he will have 4 tickets with price = 4. At last, any of the 0th, 2nd or 4th ticket seller can sell one ticket as all of them are priced at 4. Hence, the total amount after selling 3 tickets = 6 + 5 + 4 = 15.
#
# Testcase 2:
# Firstly, 0th or 2nd ticket seller can sell his one ticket at price = 5. Let us assume that 2nd ticket seller sells his ticket. Now, he would be left with 4 tickets each with price = 4. Now, 0th ticket seller will sell his one ticket at price = 5 and now he will have 4 tickets each with price = 4. Hence, the total amount after selling 2 tickets = 5 + 5 = 10.


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    tickets = list(map(int,input().split()))
    money = 0
    prices_count = [0]*(max(tickets) + 1)
    for each in tickets:
        prices_count[each] += 1
    start = max(tickets)
    for i in range(k):
        if prices_count[start] > 0:
            money += start
            prices_count[start] -= 1
            prices_count[start-1] += 1
        else:
            start -= 1
            money += start
            prices_count[start] -= 1
            prices_count[start-1] += 1
    print(money)