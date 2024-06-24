# 풀이시간 10분 시간제한 2초 메모리제한 256MB
# 1회차 정답
# 단순하게 크루스칼 알고리즘에서 각 성별이 다르게만 연결이 되게 하면되는 문제이다.

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

sex=[""]+list(map(str,input().split()))

edges=[]
for _ in range(m):
  u,v,d=map(int,input().split())
  edges.append((d,u,v))

edges.sort()

result=0
for edge in edges:
  d,u,v=edge
  if sex[u]!=sex[v] and find_parent(parent,u)!=find_parent(parent,v):
    union_parent(parent,u,v)
    result+=d

check=True
for i in range(1,n):
  if find_parent(parent,i)!=find_parent(parent,i+1):
    check=False
    break

if check:
  print(result)
else:
  print(-1)