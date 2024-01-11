# 풀이시간 10분 시간제한 1초 메모리제한 512MB
# 1회차 정답
# 각 정점을 간선으로 연결해 가면서 그것이 사이클을 이루는지 판단하는 문제이므로 union, find를 이용하는 것으로 생각이 되었다. V+Mlog2V이기 때문에 가능하다.

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
parent=[0]*n

for i in range(n):
  parent[i]=i

cycle=False
for i in range(1,m+1):
  a,b=map(int,input().split())
  if find_parent(parent,a)!=find_parent(parent,b):
    union_parent(parent,a,b)
  else:
    cycle=True
    break

if cycle:
  print(i)
else:
  print(0)