# 풀이시간 10분 시간제한 1초 메모리제한 256MB
# 1회차 정답
# 각 케이스별로 입력을 받아 각 도시가 전부 연결되는 최소 비용을 구하는 문제이므로 크루스칼 알고리즘, 즉 최소 스패닝 트리가 만들어지게 하면 된다. 이 때의 시간복잡도는 ElogE이므로 충분히 가능하다.

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

while True:
  m,n=map(int,input().split())
  if m==0 and n==0:
    break
  parent=[0]*(n+1)
  for i in range(1,n+1):
    parent[i]=i
  
  edges=[]
  for _ in range(n):
    x,y,z=map(int,input().split())
    edges.append((z,x,y))
  
  edges.sort()
  
  answer=0
  total=0
  for edge in edges:
    cost,a,b=edge
    total+=cost
    if find_parent(parent,a)!=find_parent(parent,b):
      answer+=cost
      union_parent(parent,a,b)
  
  print(total-answer)