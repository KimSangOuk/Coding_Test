# 풀이시간 15분 시간제한 2초 메모리제한 128MB
# 1회차 정답
# V의 수가 100이하이고 문제가 그래프 형태로 그려졌을 때, 최단 경로의 각 모든 나머지 지점까지의 합을 구해서 푸는 문제이기 때문에 플로이드 워셜 알고리즘을 사용하는게 적합하다.
# 그 중 최소 값이 되는 인덱스를 구하면 된다.

import sys

input=sys.stdin.readline
INF=int(1e9)

n,m=map(int,input().split())
graph=[[INF]*(n+1) for _ in range(n+1)]

for _ in range(m):
  a,b=map(int,input().split())
  graph[a][b]=1
  graph[b][a]=1

for i in range(1,n+1):
  for j in range(1,n+1):
    if i==j:
      graph[i][j]=0

for k in range(1,n+1):
  for i in range(1,n+1):
    for j in range(1,n+1):
      graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])

# for i in range(1,n+1):
#   for j in range(1,n+1):
#     if graph[i][j]==INF:
#       print("9",end=' ')
#     else:
#       print(graph[i][j],end=' ')
#   print()

min_value=INF
min_index=0
for i in range(1,n+1):
  if min_value>sum(graph[i][1:]):
    min_value=sum(graph[i][1:])
    min_index=i  

print(min_index)