# The key concept here is flipping the question 
# to formulate number of sessions required to get the optimal difficulty(maximum difference)
# i.e f(d) = (sessions[i + 1] - sessions[i] - 1 ) // d
# So Binary search for d between the limits [1, 10**9] where f(d) <= k
def f(d):
  k1 = 0
  for i in range(n-1):
    k1 += (sessions[i + 1] - sessions[i] - 1 ) // d
  if k1 <= k:
    return True
  return False

def search(left, right):
  while left < right:
    mid = (left + right) // 2
    if f(mid):
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