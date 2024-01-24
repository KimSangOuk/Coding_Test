# 풀이시간 1시간 40분 시간제한 1초 메모리제한 256MB
# 1회차 정답 - but, 시간이 오래걸려서 다시 풀기
# 모든 경우의 경로를 구하는 문제이기 전에 최단경로를 구하는 문제가 먼저 보였기에 플로이드 워셜 알고리즘을 사용하여 각 i,j까지의 최단경로를 구했다. 이때, i,j의 경로를 구해야 했는데, 직접적으로 경로를 구하려다가 불가능하다고 생각이 들어서 i,j의 경로 중 바로 다음 노드를 가리키도록 next_path에 구했다. 그 path를 추적하여 경로를 구하도록 하였다.

n=int(input())
m=int(input())

INF=int(1e9)
graph=[[INF]*(n+1) for _ in range(n+1)]

next_path=[[INF]*(n+1) for _ in range(n+1)]

for _ in range(m):
  a,b,c=map(int,input().split())
  graph[a][b]=min(graph[a][b],c)
  next_path[a][b]=b

for i in range(1,n+1):
  for j in range(1,n+1):
    if i==j:
      graph[i][j]=0

for k in range(1,n+1):
  for i in range(1,n+1):
    for j in range(1,n+1):
      if graph[i][j]>graph[i][k]+graph[k][j]:
        graph[i][j]=graph[i][k]+graph[k][j]
        next_path[i][j]=next_path[i][k]


def find_full_path(start,end):
  array=list()
  array.append(start)
  while True:
    # print(start,end)
    if start==end:
      break
    array.append(next_path[start][end])
    start=next_path[start][end]
  return len(array),array

# 최단 경로 출력
for i in range(1,n+1):
  for j in range(1,n+1):
    if graph[i][j]==INF:
      print(0,end=' ')
    else:
      print(graph[i][j],end=' ')
  print()

for i in range(1,n+1):
  for j in range(1,n+1):
    if i==j or graph[i][j]==INF:
      print(0)
    else:
      length,array=find_full_path(i,j)
      print(length,*array)
