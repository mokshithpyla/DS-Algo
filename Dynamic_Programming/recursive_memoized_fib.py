# Recursion + Memoisation ,Time Complexity: O(n)

def fib(n):
    if n in memo:
        print('memoized')
        return memo[n]
    # Base Case: 
    if n <= 2:
        return 1
    else:
        # Recursion
        f = fib(n-1)+fib(n-2)
        memo[n] = f
        return f
    # Memoization
memo={}
n=int(input("Enter the value of n: "))
print('The nth fibonacci term is:',fib(n))
