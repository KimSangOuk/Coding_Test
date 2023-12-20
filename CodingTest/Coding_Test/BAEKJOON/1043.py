# 풀이시간 30분 시간제한 2초 메모리제한 128MB
# 1회차 정답
# 거짓말을 말한 사람이 속한 집합에 각 파티에 속한 일원 중 한명이 속해있는지 구하는 문제이다. 그럴 때, 부모 노드가 같은지만 확인해서 풀 수 있기 때문에, 서로소 집합 알고리즘으로 풀어낼 수 있다. N,M이 50으로 낮기 때문에 시간복잡도 상으로도 가능하다.

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

first_lie=0
party_info=[]

for i in range(m+1):
  arr=list(map(int,input().split()))[1:]
  party_info.append(arr)
  if i==0 and len(arr)!=0:
    first_lie=arr[0]

  for j in range(len(arr)-1):
    union_parent(parent,arr[j],arr[j+1])

count=0
for party in party_info[1:]:
  answer=True
  for k in party:
    if find_parent(parent,k)==find_parent(parent,first_lie):
      answer=False
      break
  if answer:
    count+=1

print(count)