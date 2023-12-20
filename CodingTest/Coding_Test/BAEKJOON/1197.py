# 풀이시간 5분 시간제한 1초 메모리제한 128MB
# 1회차 정답
# 단순히 데이터가 100,000인 최소 스패닝 트리를 구하는 문제이므로 시간복잡도 면에서 합격이다.

import sys

input=sys.stdin.readline

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

v,e=map(int,input().split())
parent=[0]*(v+1)

for i in range(1,v+1):
  parent[i]=i

edges=[]
for _ in range(e):
  a,b,cost=map(int,input().split())
  edges.append((cost,a,b))

edges.sort()

result=0
for edge in edges:
  cost,a,b=edge
  if find_parent(parent,a)!=find_parent(parent,b):
    union_parent(parent,a,b)
    result+=cost

print(result)