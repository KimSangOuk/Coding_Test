# 풀이시간 15분/40분 시간제한 1초 메모리제한 128MB
# 1회차 정답
# N개의 여행지가 그래프 형태로 연결되어 있으며, 그 중 주어진 여행지가 전부 연결되어 있기만 하면 되는지를 구하면 되는 문제이다. 그렇게 하기 위해서는 서로소 집합을 이용해서 같은 집합에 속하는지 확인하면 되는 문제이다. 시간 복잡도는 V+Mlog2V이기 때문에 가능하다.

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

n,m=map(int,input().split())
parent=[0]*(n+1)

for i in range(1,n+1):
  parent[i]=i

graph=[]

for _ in range(n):
  graph.append(list(map(int,input().split())))

for i in range(1,n+1):
  for j in range(i,n+1):
    if graph[i-1][j-1]==1:
      union_parent(parent,i,j)

trips=list(map(int,input().split()))
answer=True
for i in range(0,len(trips)-1):
  if find_parent(parent,trips[i])!=find_parent(parent,trips[i+1]):
    answer=False

if answer==True:
  print("YES")
else:
  print("NO")