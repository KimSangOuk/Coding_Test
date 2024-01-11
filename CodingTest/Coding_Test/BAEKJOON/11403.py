# 풀이시간 10분 시간제한 1초 메모리제한 256MB
# 2회차 정답
# 그래프에서 순환이 발생할 수 있을 경우에 자기 자신까지의 거리를 0으로 취급하지 않을때의 문제이다. 이 때 각 지점에서 발생하는 그래프를 이미 다 담아서 2차원 배열로 주었기 때문에 이를 계산하는 플로이드 워셜 알고리즘만 사용하면 된다. n이 100이기 때문에 가능하다.

INF=int(1e9)
n=int(input())

graph=[]
for _ in range(n):
  graph.append(list(map(int,input().split())))

for i in range(n):
  for j in range(n):
    if graph[i][j]==0:
      graph[i][j]=INF

for k in range(n):
  for i in range(n):
    for j in range(n):
      graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])

for i in range(n):
  for j in range(n):
    if graph[i][j]==INF:
      print("0",end=' ')
    else:
      print("1",end=' ')
  print()


# 풀이시간 60분 시간제한 1초 메모리제한 256MB
# 1회차 정답 - 풀이시간 초과(30~40분 내로 풀 수 있는 문제)
# 인접 행렬을 주고 그래프의 구성을 알려준 다음, 이에 대한 최단 경로가 있는지 없는지를 구하게 하는 문제이다. V가 100이 최대이기 때문에 플로이드 워셜 알고리즘으로 풀 수 있다.
# 다만, 자기 자신에게 돌아오는 지에 대한 조건도 풀어야하는데, 이때, 자기 자신에게 돌아오기 위해서는 특정 지점으로 이동이 가능하다면 그 지점에서 다시 본래 위치로 이동이 가능해야 한다는 점을 고려하면 된다.
# 너무 문제를 얕보다가 오히려 오래걸려버렸다. 단순히 생각할 수 있는 부분이었지만 시간이 초과되었기에 다시 풀어보려고 한다.

# 1회차 풀이
# import sys

# input = sys.stdin.readline
# INF=int(1e9)

# n=int(input())

# temp=[]
# for i in range(n):
#   temp.append(list(map(int,input().split())))

# graph=[[INF]*n for _ in range(n)]
# for i in range(n):
#   for j in range(n):
#     if temp[i][j]==1:
#       graph[i][j]=1

# for i in range(n):
#   for j in range(n):
#     if i==j:
#       graph[i][j]=0

# for k in range(n):
#   for i in range(n):
#     for j in range(n):
#       graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])

# for i in range(n):
#   answer=INF
#   for j in range(n):
#     if i!=j:
#       if graph[i][j]!=INF and graph[j][i]!=INF:
#         answer=0
#   graph[i][i]=answer

# for i in range(n):
#   for j in range(n):
#     if graph[i][j]==INF:
#       print(0,end=' ')
#     else:
#       print(1,end=' ')
#   print()