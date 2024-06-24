# 풀이시간 17분 시간제한 1초 메모리제한 256MB
# 1회차 정답
# 각 양방향 연결되어 있는 간선이 정점을 연결하고, 모든 길이 이어져야 하며 왕복이 아닌 전체적인 길만을 확인한다. 또한 모든 정점이 연결되는 최소한의 간선만을 필요로 하고 있으므로 최소 스패닝 트리 알고리즘을 생각해볼 수 있다. ElogE의 시간복잡도가 필요한데 E는 V**2보다 작기 때문에 정렬시에 약 2000만회가 나오고 시간복잡도를 조금이라도 줄이기 위해 최악과 최선의 경우 정렬하기 보다는 한번 정렬하고 출력을 반대로 하는 방식을 쓰기로 했다. 또한 오르막길이 0 내리막길이 1이지만 우리는 반대로 값이 더해져서 제곱이 되어야 되기 때문에 가중치를 반대로 저장했다. 내림차순과 오름차순으로 스패닝 트리를 구한 후에 그 차를 구해주면 된다.

def find_parent(parent, x):
  if parent[x] != x:
    parent[x]=find_parent(parent, parent[x])
  return parent[x]

def union_parent(parent, a, b):
  a=find_parent(parent, a)
  b=find_parent(parent, b)
  if a<b:
    parent[b]=a
  else:
    parent[a]=b

n,m=map(int,input().split())
worst_parent=[0]*(n+1)
best_parent=[0]*(n+1)
for i in range(1,n+1):
  worst_parent[i]=i
  best_parent[i]=i

edges=[]
for _ in range(m+1):
  a,b,c=map(int,input().split())
  edges.append((int(not bool(c)),a,b))

worst=0
best=0
edges.sort()

for edge in edges:
  c,a,b=edge
  if find_parent(best_parent,a)!=find_parent(best_parent,b):
    union_parent(best_parent,a,b)
    best+=c

for i in range(len(edges)-1,-1,-1):
  c,a,b=edges[i]
  if find_parent(worst_parent,a)!=find_parent(worst_parent,b):
    union_parent(worst_parent,a,b)
    worst+=c

print(worst**2-best**2)
    