# 풀이시간 12분 시간제한 1초 메모리제한 128MB
# 1회차 정답
# 그래프 형태로 문제를 표현해 주었기에 V,E로 이루어져있는 그래프 문제로 이해할 수 있다. 이 때, 각 지점에서 모든 지점까지의 거리를 모두 구해서 비교할 필요가 있기 때문에 플로이드 워셜을 고려해볼 수 있다. 시간복잡도 또한 V가 100이하이기 때문에 가능하다.
# 그 중에서 수색 범위내에 각 지점에서의 다른 지점까지의 최단 거리가 들어왔을 때, 각 지점의 아이템 합을 구해서 그 중 최대 값을 구해서 정답으로 출력하면 된다.

import sys

input = sys.stdin.readline
INF=int(1e9)

n,m,r=map(int,input().split())
item=[0]
item+=list(map(int,input().split()))

graph=[[INF]*(n+1) for _ in range(n+1)]
for _ in range(r):
  a,b,l=map(int,input().split())
  graph[a][b]=l
  graph[b][a]=l

for i in range(1,n+1):
  for j in range(1,n+1):
    if i==j:
      graph[i][j]=0

for k in range(1,n+1):
  for i in range(1,n+1):
    for j in range(1,n+1):
      graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])

max_count=0
for i in range(1,n+1):
  count=0
  for j in range(1,n+1):
    if graph[i][j]<=m:
      count+=item[j]
  max_count=max(max_count,count)

print(max_count)