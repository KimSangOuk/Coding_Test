# 풀이시간 15분 시간제한 1초 메모리제한 256MB
# 1회차 정답
# 모든 지점이 이어지게 하면서 최소 비용을 따지고 있으므로 크루스칼 알고리즘, 즉 최소 스패닝 트리를 만드는 과정을 구한다고 생각할 수 있다. 이 때, 한 그룹에 발전소는 한개씩만 있어야하기 때문에, 부모를 발전소로 두고 발전소가 양쪽에 다 없으면 간선을 추가하는 식으로 조건을 달 수 있다. ElogE이므로 시간복잡도는 가능하다.

def find_parent(parent,x):
  if parent[x]!=x:
    parent[x]=find_parent(parent,parent[x])
  return parent[x]

def union_parent(parent,a,b):
  a=find_parent(parent,a)
  b=find_parent(parent,b)
  if a in power_plants:
    parent[b]=a
  elif b in power_plants:
    parent[a]=b
  else:
    if a<b:
      parent[b]=a
    else:
      parent[a]=b

n,m,k=map(int,input().split())
parent=[0]*(n+1)
for i in range(1,n+1):
  parent[i]=i

power_plants=set(list(map(int,input().split())))

edges=[]
for _ in range(m):
  a,b,c=map(int,input().split())
  edges.append((c,a,b))

edges.sort()
result=0

for edge in edges:
  cost,a,b=edge
  if find_parent(parent,a)!=find_parent(parent,b) and (find_parent(parent,a) not in power_plants or find_parent(parent,b) not in power_plants):
    union_parent(parent,a,b)
    result+=cost

print(result)