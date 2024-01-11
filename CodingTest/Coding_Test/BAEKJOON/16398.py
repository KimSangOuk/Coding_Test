# 풀이시간 10분 시간제한 1초 메모리제한 256MB
# 1회차 정답
# 단순히 2차원배열을 각 간선과 비용으로 바꾸어서 모든 지점을 연결하는 최소비용을 구하는 최소 스패닝 트리, 크루스칼 알고리즘을 사용하면 된다. ElogE 이기 때문에 모든 지점이 각 서로 연결되어있다해도 가능하다.
def find_parent(parent,x):
  if parent[x]!=x:
    parent[x]=find_parent(parent,parent[x])
  return parent[x]

def union_parent(parent,a,b):
  a=find_parent(parent,a)
  b=find_parent(parent,b)
  if a<b:
    parent[b]=a
  else:
    parent[a]=b

n=int(input())
parent=[0]*(n+1)
for i in range(1,n+1):
  parent[i]=i

graph=[]
for i in range(n):
  graph.append(list(map(int,input().split())))

edges=[]
for i in range(0,n):
  for j in range(i+1,n):
    edges.append((graph[i][j],i+1,j+1))

edges.sort()

answer=0
for edge in edges:
  cost,a,b=edge
  if find_parent(parent,a)!=find_parent(parent,b):
    answer+=cost
    union_parent(parent,a,b)

print(answer)