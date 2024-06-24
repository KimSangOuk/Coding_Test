# 풀이시간 2시간/60분 시간제한 1초 메모리제한 256MB
# 2회차 오답
# 정점과 간선을 준 트리 형태에서 트리의 갯수를 구하는 문제이다. 즉 순환하지 않는 집합이 몇개있는지 구하는 문제이기 때문에 find, union 연산으로 접근했다. 시간복잡도는 가능하다. 이 때, 매순간 간선을 연결해 나가는데 이 때, 두 정점이 이미 소속 그룹이 같을 경우 순환이 이루어질 것이기 때문에 그 정점을 set에 저장해둔다. 그리고 둘 중 하나의 정점이 순환을 이루고 있는집합일 경우, 그 두개의 정점 또한 set에 저장해두면 된다. 그리고 난 뒤에 저장된 set를 확인하며 현재 확인하고 있는 집합이 순환하는지 확인하며 숫자를 세면 된다. 이렇게 되는 이유는 두 정점이 연결될 때 순환이 되는 경우는 두가지 이기 때문이다. 첫번재는 이미 연결되어 있을 경우에 한번 더 연결되면 순환이 된다. 두 번째는, 연결이 되어 있지 않더라도 한쪽 그룹이 순환하면 연결 후에 순환이 되기 때문이다. 이 때, union 연산을 뒤쪽에 해주어야 하는데 union 연산을 해버리면 parent가 a,b가 같은 것으로 연결이 먼저 되버린 상태가 되기 때문에 순환을 확인하거나 확인하는 등의 parent를 통한 연산을 해줄 수가 없다.
# 왜 틀렸는가? 먼저 이어지지 않을 경우 이어주는 연산을 하고 이어져있다면 굳이 이어주지 않고 사이클에 담는 연산을 했는데 이렇게 되면 이어지지 않은 상태에서 한쪽이 사이클이 발생하여 연결시 사이클이 되는 경우가 생길 수 있기 때문에 이 때 사이클을 분별하는 집합에 넣는 연산이 빠지게 된다. 왜 이부분을 생각하지 못했는가? 무조건적으로 아닐 경우, 연결하고 연결되어 있으면 순환이 발생한다고만 생각했기 때문에 이런식의 계산을 했는데 한쪽이 순환이 되는 경우에 연결하면 그 순환하는 집합에 포함되는 연산 또한 해주어야 한다는 것을 생각하지 못했다. 왜 그런 생각을 못했는가? 단순 parent연산을 하면 부모가 같아지기 때문에 필요없다고 생각을 했지만 부모가 같아져도 그 순환하지 않는 parent가 더 작아서 parent로 업데이트 되면 순환하는 집합의 parent는 업데이트 되지 않기 때문에 곤란해진다. 왜 이 생각을 하지 못했는가? 역시나 단순하게 연결시에만 넣으면 된다는 편견에 갇혀있었기 때문이다. 그렇기 때문에 다음부터는 순환을 판단할 떄 이부분을 생각해야 한다는 것을 인지하고 있어야 한다.

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
  cycle=set()
  for _ in range(m):
    a,b=map(int,input().split())
    if find_parent(parent,a)==find_parent(parent,b):
      cycle.add(parent[a])
      cycle.add(parent[b])
    if parent[a] in cycle or parent[b] in cycle:
      cycle.add(parent[a])
      cycle.add(parent[b])
    union_parent(parent,a,b)

  for i in range(1,n+1):
    find_parent(parent,i)

  parent=list(set(parent[1:]))
  tree_count=len(parent)
  for k in parent:
    if k in cycle:
      tree_count-=1

  if tree_count<=0:
    print("Case "+str(tc)+": No trees.")
  elif tree_count==1:
    print("Case "+str(tc)+": There is one tree.")
  else:
    print("Case "+str(tc)+": A forest of "+str(tree_count)+" trees.")



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
