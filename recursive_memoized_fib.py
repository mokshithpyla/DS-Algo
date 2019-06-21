def fib(n):
    if n in memo:
        return memo[n]
    if n<=2:
        return 1
    else:
        f=fib(n-1)+fib(n-2)
        return f
    memo[n]=f
memo={}
n=int(input("Enter the value of n: "))
print('The nth fibonacci term is:',fib(n))
