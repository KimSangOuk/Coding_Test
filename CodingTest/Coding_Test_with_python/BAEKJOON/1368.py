# 풀이시간 50분 시간제한 2초 메모리제한 128MB
# 1회차 정답
# 우물에 물을 대는 경우는 정점에 우물을 파거나 다른 곳에서 끌어오거나 둘 중 하나이다. 이 때, 모든 정점에 물을 대야 하므로 모두 연결되거나 연결되지 않은 곳은 우물을 파야한다. 모두 우물을 파지 않고 물을 끌어와서 댈 경우 경로의 가중치의 합이 최소가 되는 경우로 최소 스패닝 트리이다. 하지만 현재 연결되고 있는 집단의 최소 비용과 연결하고자 하는 집단의 최소비용의 합, 즉 연결하지 않고 각 집단에 우물이 있어서 연결을 할 필요가 없는 경우가 각 집단을 합치는 경우보다 작으면 연결을 하지 않는 편이 총 비용이 적게 드므로 그렇지 않은 경우에만 연결하면 된다. 이때 연결을 해주면 되는데 연결을 할 때, parent의 값은 집단의 종류를 나타내기 때문에 새롭게 각 집단이 연결될 때의 최소 우물 비용과 집단의 총 비용 또한 parent값과 같이 합쳐질 때 갱신하면 된다. 시간제한이 2초이기 때문에 연산이 약 4000만회 정도 이루어질 수 있는데 n이 300이므로 간선의 갯수는 90,000보다 작기 때문에 ElogE는 가능하지만 우리는 집단 별 최소 비용과 우물의 최소 비용 또한 *n회로 갱신 시켜주어야 하므로 27,000,000회 정도 이루어진다고 할 수 있기 때문에 충분히 가능하다.

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
parent=[0]*(n)
cost_well=[]
cost_set=[]
for i in range(n):
  parent[i]=i
  k=int(input())
  cost_well.append(k)
  cost_set.append(k)

edges=[]
for i in range(n):
  array=list(map(int,input().split()))
  for j in range(i+1,n):
    edges.append((array[j],i,j))

edges.sort()

for edge in edges:
  cost,a,b=edge
  if find_parent(parent,a)!=find_parent(parent,b):
    if cost_set[a]+cost_set[b]>=cost_set[a]+cost_set[b]-cost_well[a]-cost_well[b]+min(cost_well[a],cost_well[b])+cost:
      union_parent(parent,a,b)
      min_well=min(cost_well[a],cost_well[b])
      cost_set_one=cost_set[a]+cost_set[b]-cost_well[a]-cost_well[b]+min_well+cost
      cost_well_one=min_well
      for i in range(n):
        if find_parent(parent,i)==find_parent(parent,a):
          cost_set[i]=cost_set_one
          cost_well[i]=cost_well_one

for i in range(n):
  find_parent(parent,i)

set_type=set(parent)
result=0
for k in set_type:
  result+=cost_set[k]

print(result)