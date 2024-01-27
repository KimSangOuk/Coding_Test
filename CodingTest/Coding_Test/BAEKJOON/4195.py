# 풀이시간 23분 시간제한 3초 메모리제한 256MB
# 1회차 정답
# 친구 관계가 연결되고 현재 연결된 상태에서의 집합의 수를 구하는 거기 때문에 union_find로 접근해볼 수 있다고 생각할 수 있다. E가 100,000이기 때문에 친구가 전부 다를 경우 최대 V가 200,000이라고 생각해둔다. 이 때, parent를 숫자로 받을 시 x와 parent[x]값이 달라지기 때문에 처리가 힘들기 때문에 x를 문자열로 받을 생각으로 parent를 딕테이션으로 지정해서 받는다. 처음 들어오는 이름이 있을 경우 parent를 자기 자신으로 지정하면 된다. 그리고 우리는 집합에 친구가 될 시 친구를 넣어서 숫자를 세거나 친구만 더해가면서 하면 되는데 10만개의 간선을 받을 때 집합으로 받아놓으면 또다시 탐색을 친구 수만큼 해야될 수 있기 때문에 단순히 친구이름에 따라 숫자로 받을 생각을하고 딕테이션을 하나 더 만든다. 이 경우도 똑같이 친구가 새롭게 들어오면 수를 1로 지정한다. 어차피 들어올때마다 합쳐야 하므로 union을 뒤로 빼고 union후에 둘중하나의 부모를 찾아서 친구수를 출력하면 된다. 합치기 전에 우리는 친구수가 합쳐지는 것을 각자에서 찾아서 더해야하므로 각 부모를 찾아서 친구수를 찾은 다음 각 부모에 다시 저장해주면 된다. 시간복잡도는 반복문이 따로 추가되면서 늘어나지 않기 때문에 V+MlogV로 풀 수 있다.

def find_parent(parent,x):
  if parent[x]!=x:
    parent[x]=find_parent(parent,parent[x])
  return parent[x]

def union_parent(parent,a,b):
  a=find_parent(parent,a)
  b=find_parent(parent,b)
  arr=[a,b]
  arr.sort()
  if arr[0]==a:
    parent[b]=a
  else:
    parent[a]=b

for tc in range(int(input())):
  f=int(input())
  parent=dict()
  friend=dict()
  for i in range(1,f+1):
    a,b=map(str,input().split())
    if a not in parent:
      parent[a]=a
      friend[a]=1
    if b not in parent:
      parent[b]=b
      friend[b]=1
    a_p=find_parent(parent,a)
    b_p=find_parent(parent,b)
    if a_p!=b_p:
      friend[a_p]+=friend[b_p]
      friend[b_p]=friend[a_p]

    union_parent(parent,a,b)
    print(friend[a_p])

# 풀이시간 2시간/50분 시간제한 1초 메모리제한 256MB
# 1회차 정답 - But, 풀이시간이 너무 오래 걸려서 재풀이
# 먼저 갯수를 처리하는데 시간이 너무 오래 걸렸다. 알고리즘 적으로 count를 세는 데 O(N)이 쓰이면 안되는 것을 알고 이것을 union_parent에 적용해야 겠다. 이 판단을 하는데 너무 오래걸렸다. 그리고 count를 union 함수로 처리하고 나서 또 오답 판정을 받아서 이유를 찾는데 한시간이 걸렸는데, 친구가 새로 생기는 경우가 아니더라도 관계와 네트워크는 다른 별개의 것이었다. 즉, 집합에 속하는 것과 간선의 차이였는데, 표현이 그렇다보니 이 부분을 캐치하지 못했다.
# 먼저 두번째 문제점 같은 경우, 간선과 집합의 표현이 서로 관계를 표현하는 표현이다보니 헷갈릴 수 있으니 정확히 구분해서 문제에 접근하면 될 것 같다.
# 첫번째로 시간이 오래 걸린 문제는, count 해결 관련인데, 지금까지는 union-find 함수를 건드리는 문제가 없었기에 내가 건드리는데 거부감이 생겨서 오래걸린 것도 있다. 이 문제는 이번에 맞닿드려서 해결했으니 괜찮다.

# 1회차 풀이
# import sys

# input=sys.stdin.readline

# def find_parent(parent,x):
#   if parent[x]!=x:
#     parent[x]=find_parent(parent,parent[x])
#   return parent[x]

# def union_parent(count,parent,a,b):
#   a=find_parent(parent,a)
#   b=find_parent(parent,b)
#   if a<b:
#     parent[b]=a
#     count[a]+=count[b]
#     count[b]=0
#   elif a>b:
#     parent[a]=b
#     count[b]+=count[a]
#     count[a]=0
#   # if a!=b:
#   #   parent[b]=a
#   #   count[a]+=count[b]
#   #   count[b]=0

# for tc in range(int(input())):
#   f=int(input())
#   parent=dict()
#   count=dict()
#   for _ in range(f):
#     a,b=map(str,input().split())
#     if a not in parent:
#       parent[a]=a
#       count[a]=1
#     if b not in parent:
#       parent[b]=b
#       count[b]=1
      
#     union_parent(count,parent,a,b)
#     print(count[find_parent(parent,a)])