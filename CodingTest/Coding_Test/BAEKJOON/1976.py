# 풀이시간 20분 시간제한 2초 메모리제한 128MB
# 1회차 정답
# 도시가 전부 이어져 있는지 확인하는 문제인데다가 도시들이 이어져 있는 길이 있어, 데이터가 그래프 형태이기 때문에, disjoint set 알고리즘을 이용하여 여행 계획에 있는 도시들이 서로 이어져 있는지 확인하면 된다. 시간복잡도 상으로도 가능하다.

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

for i in range(1,n+1):
  arr=list(map(int,input().split()))
  for j in range(i+1,n+1):
    if arr[j-1]==1:
      union_parent(parent,i,j)

trips=list(map(int,input().split()))
answer=True
for i in range(m-1):
  if find_parent(parent,trips[i])!=find_parent(parent,trips[i+1]):
    answer=False
    break
if answer:
  print("YES")
else:
  print("NO")