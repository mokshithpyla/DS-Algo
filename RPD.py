# cook your dish here
def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s
t = int(input())
for _ in range(t):
    n = int(input())
    numbers = list(map(int, input().split()))
    memo = {}
    sum_of_product = 0
    max_digit_sum = 0
    for i in range(n-1):
        for j in range(i+1, n):
            if (numbers[i], numbers[j]) in memo:
                continue
            product = numbers[i] * numbers[j]
            sum_of_product = sum_digits(product)
            memo[(i, j)] = memo[(j, i)] = sum_of_product
            max_digit_sum = max(sum_of_product, max_digit_sum)
    print(max_digit_sum)

