# 풀이시간 60분 시간제한 2초 메모리제한 128MB
# 1회차 정답
# 각 장소의 최소 시간을 2차원 배열로 주었기 때문에 플로이드 워셜 알고리즘의 결과를 받은 것과 같다고 할 수 있다. 플로이드 워셜을 생각했을 때, 각 최단 거리이므로 각 정점으로부터의 서로의 최단거리를 표를 보고 이은 거라고 생각해도 이상이 없다. 이 때, 우리는 최소한의 도로의 갯수가 필요하므로 표를 만드는 필요 이상의 도로는 필요 없기 때문에 도로를 줄여야 된다고 생각할 수 있다. 이 때, 쌍의 합도 최솟값이 되야 하므로 작은 것부터 도로를 깐다고 했을 때, 현재 추가 된 노선이 최단 노선이 될 때만 추가 하고, 그 이외에는 추가하면 안된다는 것을 알 수 있다. 필요한 노선들을 깔고 최종 결과가 처음에 주어진 플로이드 워셜 2차원 배열의 결과와 같아야 하므로 결과가 같다면 깔은 노선들의 가중치의 합을 다르다면 -1을 출력하면 된다.

n=int(input())

INF=int(1e9)
graph=[]
for i in range(n):
  graph.append(list(map(int,input().split())))

edges=[]
for i in range(n):
  for j in range(i+1,n):
    if i!=j:
      edges.append((i,j,graph[i][j]))

edges.sort(key=lambda x:x[2])

new_graph=[[INF]*(n) for _ in range(n)]

for i in range(n):
  for j in range(n):
    if i==j:
      new_graph[i][j]=0

count=0
value=0
for edge in edges:
  for k in range(n):
    for i in range(n):
      for j in range(n):
        new_graph[i][j]=min(new_graph[i][j],new_graph[i][k]+new_graph[k][j])
  if new_graph[edge[0]][edge[1]]!=edge[2]:
    new_graph[edge[0]][edge[1]]=edge[2]
    new_graph[edge[1]][edge[0]]=edge[2]
    value+=edge[2]

for k in range(n):
  for i in range(n):
    for j in range(n):
      new_graph[i][j]=min(new_graph[i][j],new_graph[i][k]+new_graph[k][j])

possible=True
for i in range(n):
  for j in range(n):
    if new_graph[i][j]!=graph[i][j]:
      possible=False
if possible:
  print(value)
else:
  print(-1)