# 풀이시간 30분 시간제한 1초 메모리제한 256MB
# 1회차 정답
# 단순히 비교를 안한 횟수를 얻어내는 플로이드 워셜 알고리즘 문제

n=int(input())

m=int(input())

INF=int(1e9)
graph=[[INF]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
  for j in range(1,n+1):
    if i==j:
      graph[i][j]=0

for _ in range(m):
  a,b=map(int,input().split())
  graph[a][b]=1

for k in range(1,n+1):
  for i in range(1,n+1):
    for j in range(1,n+1):
      graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])

for i in range(1,n+1):
  count=0
  for j in range(1,n+1):
    if graph[i][j]>=INF and graph[j][i]>=INF:
      count+=1
  print(count)