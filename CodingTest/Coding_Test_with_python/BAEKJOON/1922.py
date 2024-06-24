# 풀이시간 10분 시간제한 2초 메모리제한 256MB
# 1회차 정답
# 단순히 그래프의 간선을 주어지고 그 중 합이 최소가 되는 모두 연결되는 그래프를 만드는 최소 스패닝 트리의 문제이다. 간선의 개수가 100,000개 이기 때문에 시간복잡도 상으로 가능하다.

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

n=int(input())
m=int(input())
parent=[0]*(n+1)

for i in range(1,n+1):
  parent[i]=i

edges=[]
for _ in range(m):
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