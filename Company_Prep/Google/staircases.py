def solution(n):
    # Your code here
    cache = [[0 for i in range(n + 2)] for j in range(n + 2)]
    return diffNumOfStaircases(1, n, cache) - 1
def diffNumOfStaircases(height, length, cache):
    if cache[height][length] != 0:
        return cache[height][length]
    if length == 0:
        return 1
    if length < height:
        return 0
    cache[height][length] = diffNumOfStaircases(height + 1, length - height, cache) + diffNumOfStaircases(height + 1, length, cache)
    return cache[height][length]