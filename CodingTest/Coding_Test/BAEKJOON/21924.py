# 풀이시간 15분 시간제한 1초 메모리제한 512MB
# 1회차 정답
# 각 도시가 연결되어있을 때, 그 때의 도시를 잇는 간선간의 가중치의 합을 최소화 하므로 최소 스패닝 트리를 만드는 방법으로 만들어내면 된다. 이때, 도시가 전부 연결되지 않았을 때를 추가적으로 찾아야 하므로, 연결을 하고 나서 전부 연결이 되어 있는지 find_parent를 통해 전부 같은지 확인하면 된다. 시간복잡도는 ElogE로 가능하다.

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

n,m=map(int,input().split())
parent=[0]*(n+1)

for i in range(1,n+1):
  parent[i]=i

edges=[]
for _ in range(m):
  a,b,c=map(int,input().split())
  edges.append((c,a,b))

edges.sort()
result=0
for edge in edges:
  cost,a,b=edge
  if find_parent(parent,a)!=find_parent(parent,b):
    union_parent(parent,a,b)
  else:
    result+=cost

all_connect=True
for i in range(1,n):
  if find_parent(parent,i)!=find_parent(parent,i+1):
    all_connect=False
    break

if all_connect:
  print(result)
else:
  print(-1)