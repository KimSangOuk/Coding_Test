# 풀이시간 25분 시간제한 2초 메모리제한 128MB
# 1회차 정답
# 이미 연결된 부분은 연결시키고 새롭게 구하는 간선 중에서 전부 이어지도록 하는 문제이다. 그렇기에 크루스칼 알고리즘을 생각해볼 수 있다. 이 때, 이미 이어지고 난 나머지 중 사이클을 이루지 않게 하는 간선 중 cost가 작은 값부터 하나씩 넣어가면 된다.

import math

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

def get_dist(pos1,pos2):
  x1,y1=pos1
  x2,y2=pos2
  return math.sqrt(abs(x1-x2)**2+abs(y1-y2)**2)

n,m=map(int,input().split())
parent=[0]*(n+1)
for i in range(1,n+1):
  parent[i]=i

pos=[]
for _ in range(n):
  pos.append(tuple(map(int,input().split())))

for i in range(m):
  a,b=map(int,input().split())
  union_parent(parent,a,b)

edges=[]
for i in range(1,n):
  for j in range(i+1,n+1):
    if find_parent(parent,i)!=find_parent(parent,j):
      cost=float(get_dist(pos[i-1],pos[j-1]))
      edges.append((cost,i,j))

edges.sort()
result=0
for edge in edges:
  cost,a,b=edge
  if find_parent(parent,a)!=find_parent(parent,b):
    union_parent(parent,a,b)
    result+=float(cost)

print(format(result, ".2f"))