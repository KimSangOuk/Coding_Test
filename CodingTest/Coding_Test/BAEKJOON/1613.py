# 풀이시간 30분 시간제한 1초 메모리제한 128MB
# 1회차 정답
# 플로이드 워셜 알고리즘으로 전체에서 전체로 가는 경우를 구한다음 비교의 크기에 따라 1,-1,0을 출력해주면 되는 문제이다.

n,k=map(int,input().split())

INF=int(1e9)
graph=[[INF]*(n+1) for _ in range(n+1)]

for i in range(n+1):
  for j in range(n+1):
    if i==j:
      graph[i][j]=0

for _ in range(k):
  a,b=map(int,input().split())
  graph[a][b]=1

for k in range(1,n+1):
  for i in range(1,n+1):
    for j in range(1,n+1):
      graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])

s=int(input())

for _ in range(s):
  a,b=map(int,input().split())
  if graph[a][b]<INF:
    print(-1)
  elif graph[b][a]<INF:
    print(1)
  else:
    print(0)