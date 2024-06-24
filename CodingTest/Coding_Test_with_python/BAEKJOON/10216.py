# 풀이시간 15분 시간제한 8초 메모리제한 256MB
# 1회차 정답
# 각 원이 접촉하거나 영역이 겹치면 같은 집합으로 묶고 해당 집합이 몇개있는지 물어보믄 서로소 집합 문제이다. 그렇기 때문에 find_union 연산을 이용해서 영역이 겹칠 시에만 union해서 집합의 개수를 구해내면 된다. 총 n이 3,000이기 때문에 V+Mlog2V로 가능하다.

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
  return math.sqrt(abs(pos1[0]-pos2[0])**2+abs(pos1[1]-pos2[1])**2)

for tc in range(int(input())):
  n=int(input())
  parent=[0]*(n+1)
  for i in range(1,n+1):
    parent[i]=i

  pos=[]
  for _ in range(n):
    pos.append(tuple(map(int,input().split())))

  pos=[0]+pos

  for i in range(1,n):
    for j in range(i+1,n+1):
      if get_dist(pos[i],pos[j])<=pos[i][2]+pos[j][2]:
        union_parent(parent,i,j)

  for i in range(1,n+1):
    find_parent(parent,i)

  count=[0]*(n+1)
  for i in range(1,n+1):
    count[parent[i]]+=1

  answer=0
  for i in range(1,n+1):
    if count[i]>0:
      answer+=1
  print(answer)