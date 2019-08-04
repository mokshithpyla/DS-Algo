# cook your dish here
t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    max_points = 0
    for i in range(n):
        goal_points = A[i] * 20
        foul_points = B[i] * 10
        points_secured = goal_points - foul_points
        if points_secured > 0:
            max_points = max(max_points, points_secured)
    print(max_points)

