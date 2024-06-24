# 풀이시간 15분 시간제한 2초 메모리제한 512MB
# 1회차 정답
# 각 어떤 집합으로 나누어지고 그 집합에서의 문제를 해결하는 유형이므로 각 집합을 만들어내는 find_union을 이용하면 된다. 시간복잡도는 V+Mlog2V이므로 가능하다. 이 때, parent를 이용해야 하기 때문에 한번 더 확실한 parent 값을 저장하기 위해 parent를 한번 더 돌려준 후, 각 그룹의 멤버를 따로 저장해 값을 구해내면 된다.

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

n,m,k=map(int,input().split())
parent=[0]*(n+1)

cost=[0]+list(map(int,input().split()))
for i in range(1,n+1):
  parent[i]=i

for _ in range(m):
  a,b=map(int,input().split())
  if find_parent(parent,a)==find_parent(parent,b):
    continue
  else:
    union_parent(parent,a,b)

for i in range(1,n+1):
  find_parent(parent,i)

group=[[] for _ in range(n+1)]
for i in range(1,n+1):
  group[parent[i]].append(i)

# print(group)

money=0
for i in range(1,n+1):
  total_cost=int(1e9)
  for t in group[i]:
    total_cost=min(total_cost,cost[t])
  if total_cost<int(1e9):
    money+=total_cost

if money<=k:
  print(money)
else:
  print("Oh no")