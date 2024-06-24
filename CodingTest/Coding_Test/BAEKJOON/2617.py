# 풀이시간 15분 시간제한 1초 메모리제한 128MB
# 1회차 정답
# 구슬의 비교를 표로 나타내면 플로이드 워셜 알고리즘을 통해 연산을 나타내는 것과 마찬가지인데, 이 때, 한쪽에서의, 즉, 크거나 작은 갯수가 중간이 될 수 있는 횟수가 크다면 그 수는 중간이 될 수 없기 때문에 그 수를 구해주면 된다. 시간복잡도는 데이터의 크기가 100이기 때문에 가능하다.

n,m=map(int,input().split())

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

answer=0
for i in range(1,n+1):
  count=0
  for j in range(1,n+1):
    if graph[i][j]<INF:
      count+=1
  if count>(n+1)//2:
    answer+=1

for j in range(1,n+1):
  count=0
  for i in range(1,n+1):
    if graph[i][j]<INF:
      count+=1
  if count>(n+1)//2:
    answer+=1

print(answer)