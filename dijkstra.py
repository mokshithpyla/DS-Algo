# Logical Error! in Dijkstra
def findMin(distance,visited,n):
    minVertex=-1
    for i in range(1,n+1):
        if visited[i]==False and  minVertex == -1 or distance[i]<distance[minVertex]:
            minVertex=i
    return minVertex

def dijkstra(weight,n,s):
    distance=[100]*(n+1)
    visited=[False]*(n+1)
    distance[s]=0
    for i in range(1,n+1):
        minVertex = findMin(distance,visited,n)
        visited[minVertex]=True
        for j in range(1,n+1):
            if weight[minVertex][j] != 0 and visited[j] == False:
                dist = weight[minVertex][j] + distance[minVertex]
                if dist < distance[j]:
                    distance[j] = dist
    for i in range(1,n+1):
        print(i, distance[i])
n=int(input('Enter number of nodes: '))
weight=[['X', 'X', 'X', 'X', 'X']]
print('Enter Distances in matrix form: ')
for i in range(1,n+1):
    weight.append(list(map(int,input().split())))
    weight[i].insert(0,'X')
s=int(input('Enter the source vertex: '))
dijkstra(weight,n,s)

 # 0 5 2 6
 # 5 0 2 0
 # 2 3 0 1
 # 6 0 1 0