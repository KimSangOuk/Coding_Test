# 풀이시간 90분/60분 시간제한 1초 메모리제한 256MB
# 1회차 정답
# find_union 연산으로 사이클을 구하고 parent를 구할 때의 한계를 보여주는 문제이다. 한번의 union이 간선 수 만큼 끝나도 한번에 parent가 재정립이 되지 않을 수 있으며 그렇기 때문에, cycle이 발생하는 경우를 찾아도 바로 원하는 parent를 구할 수 없을 수 있다는 점을 깨달았다. 그렇기 때문에 한번 전체적으로 수행해주어야 우리가 원하는 답이 나올 수 있다.
# 이 때문에 풀이시간에서 오래 걸린 문제이다.
# 우리가 원하는 답을 구하기 위해 find의 연산이 하나의 정답을 찾아내는데 두번이상 이루어지지 않는다면 이부분을 의심해볼 수 있다.

from collections import deque

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

tc=0
while True:
  tc+=1
  n,m=map(int,input().split())
  if n==0 and m==0:
    break
  parent=[0]*(n+1)
  for i in range(1,n+1):
    parent[i]=i
  cycle=set([])
  for _ in range(m):
    a,b=map(int,input().split())
    if find_parent(parent,a)==find_parent(parent,b):
      cycle.add(find_parent(parent,a))
    else:
      union_parent(parent,a,b)

  for i in range(1,n+1):
    find_parent(parent,i)
  cycle=deque(list(cycle))
  for i in range(len(cycle)):
    k=cycle.popleft()
    cycle.append(find_parent(parent,k))

  print("Case "+str(tc)+":",end=" ")

  answer=[0]*(n+1)
  for i in range(1,n+1):
    answer[parent[i]]+=1
  # print(parent)
  # print(answer)
  # print(cycle)
  count=0

  for i in range(1,n+1):
    if answer[i]>0 and find_parent(parent,i) not in cycle:
      count+=1
  if count==0:
    print("No trees.")
  elif count==1:
    print("There is one tree.")
  else:
    print("A forest of "+str(count)+" trees.")
