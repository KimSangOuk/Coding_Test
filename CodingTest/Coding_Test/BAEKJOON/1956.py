# 풀이시간 10분 시간제한 2초 메모리제한 128MB
# 1회차 정답
# 문제에서 사이클이 이루어지는 즉, 갔다가 올 수 있는 최단 거리를 구하라고 하였으므로 모든 지점의 최단 거리가 있는 편이 편하며, V의 값도 플로이드 워셜 알고리즘의 시간복잡도를 충분히 만족시킨다.
# 오고 가는 길의 합은 어짜피 같기 때문에 두 길이 존재할 때, 최소값을 구하면 된다.

import sys

input=sys.stdin.readline
INF=int(1e9)

v,e=map(int,input().split())
graph=[[INF]*(v+1) for _ in range(v+1)]

for _ in range(e):
  a,b,c=map(int,input().split())
  graph[a][b]=c

for i in range(1,v+1):
  for j in range(1,v+1):
    if i==j:
      graph[i][j]=0

for k in range(1,v+1):
  for i in range(1,v+1):
    for j in range(1,v+1):
      graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])

answer=INF
for i in range(2,v+1):
  for j in range(i+1,v+1):
    if graph[i][j]!=INF and graph[j][i]!=INF:
      answer=min(answer,graph[i][j]+graph[j][i])

if answer==INF:
  print(-1)
else:
  print(answer)