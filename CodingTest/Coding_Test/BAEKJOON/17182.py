# 풀이시간 15분 시간제한 1초 메모리제한 512MB
# 1회차 정답
# 각 위치에서 이동가능한 노선들과 가중치를 주었기 때문에 우리는 그래프를 그릴 수 있고 모든 출발점에서 도착점까지의 최단거리를 구한 다음 모든 노드를 들린다고 가정하고 순열로 케이스를 모두 탐색해 최소가 되는 경로를 찾을 수 있다고 생각할 수 있다. 시간복잡도는 행성이 모두 10개밖에 안되므로 n^3이 충분히 가능하고 시작점을 제외한 나머지 최대 9개를 순열로 케이스를 나누어도 전부가능하고 메모리도 충분하다는 것을 알 수 있다.

from itertools import permutations

n,s=map(int,input().split())

INF=int(1e9)

graph=[[INF]*(n) for _ in range(n)]

for i in range(0,n):
  array=list(map(int,input().split()))
  for j in range(0,n):
    graph[i][j]=array[j]
  
for i in range(n):
  for j in range(n):
    if i==j:
      graph[i][j]=0

for k in range(n):
  for i in range(n):
    for j in range(n):
      graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])

planet=[i for i in range(n) if i!=s]
result=INF
for case in list(permutations(planet,len(planet))):
  start=s
  path=0
  for i in case:
    path+=graph[start][i]
    start=i
  result=min(result,path)

print(result)

