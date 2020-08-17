def check(diff):
  k1 = 0
  for i in range(n-1):
    k1 += (sessions[i + 1] - sessions[i] - 1 ) // diff
  if k1 <= k:
    return True
  return False

def search(left, right):
  while left < right:
    mid = (left + right) // 2
    if check(mid):
      right = mid
    else:
      left = mid + 1
  return left # or right

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    sessions = list(map(int, input().split()))
    ans = search(1, 10**9)
    print("Case #{}: {}".format(_+1, ans))