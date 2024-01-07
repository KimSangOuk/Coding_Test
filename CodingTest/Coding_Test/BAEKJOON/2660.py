# 풀이시간 15분 시간제한 1초 메모리제한 128MB
# 1회차 정답
# 각 점수는 어떤 친구와 다른 친구들 사이의 거리 중 최대값을 나타내기 때문에 모든 친구의 점수를 구한다음 그 중 점수가 가장 낮은 사람의 점수와 그 수, 그리고 그 목록을 출력하면 된다.
# 이 때, 각 사이의 모든 최단 거리를 구해야 그 중 최댓값을 구할 수 있기 때문에 플로이드 워셜 알고리즘을 사용하여 모든 관계의 최단 거리를 구하여 사용할 수 있다. 친구의 수는 50명이 최대이기 때문에 O(N^3)의 시간복잡도로 가능하다.

n=int(input())

INF=int(1e9)
graph=[[INF]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
  for j in range(1,n+1):
    if i==j:
      graph[i][j]=0

while True:
  a,b=map(int,input().split())
  if a==-1 and b==-1:
    break
  graph[a][b]=1
  graph[b][a]=1

for k in range(1,n+1):
  for i in range(1,n+1):
    for j in range(1,n+1):
      graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])

score=[0]*(n+1)
for i in range(1,n+1):
  for j in range(1,n+1):
    if graph[i][j]!=INF:
      score[i]=max(score[i],graph[i][j])

# print(score)

print(min(score[1:]),score.count(min(score[1:])))
for i in range(1,n+1):
  if score[i]==min(score[1:]):
    print(i,end=' ')