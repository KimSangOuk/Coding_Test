# 풀이시간 27분 시간제한 1초 메모리제한 256MB
# 1회차 정답
# 방향이 적힌 대로 이동해서 이었을 때, 구간이 몇개로 나눠지는지 문제이므로 서로소 집합 문제로 생각해 볼 수 있다. 각 find와 union을 2차원 배열의 위치를 가리키도록 바꾸고 현재 위치와 가리키는 위치를 집합으로 묶어가며 모든 2차원 배열을 탐색하면 된다. 이때, 이미 묶인 곳은 다시 묶을 필요는 없기 때문에 안묶인 곳만 진행한다. find를 통해 처음 으로 리셋하기 위해 find를 전체적으로 한번 더 진행하고 총 몇개의 집합이 나오는지 같은 원소의 종류가 몇개인지 확인해주면 된다.

n,m=map(int,input().split())

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def change_dir(c):
  if c=='U':
    return 0
  elif c=='D':
    return 1
  elif c=='L':
    return 2
  elif c=='R':
    return 3

board=[]
for i in range(n):
  board.append(list(input()))

def find_parent(parent,x):
  if parent[x[0]][x[1]]!=[x[0],x[1]]:
    parent[x[0]][x[1]]=find_parent(parent,parent[x[0]][x[1]])
  return parent[x[0]][x[1]]

def union_parent(parent,a,b):
  a=find_parent(parent,a)
  b=find_parent(parent,b)
  arr=[a,b]
  arr.sort()
  if arr[0]==a:
    parent[b[0]][b[1]]=a
  else:
    parent[a[0]][a[1]]=b


parent=[[[0]*2 for _ in range(m)] for _ in range(n)]

for i in range(n):
  for j in range(m):
    parent[i][j]=[i,j]

for i in range(n):
  for j in range(m):
    dir=change_dir(board[i][j])
    next=[i+dx[dir],j+dy[dir]]
    if find_parent(parent,next)!=find_parent(parent,[i,j]):
      union_parent(parent,next,parent[i][j])

answer=set()
for i in range(n):
  for j in range(m):
    find_parent(parent,[i,j])
    answer.add(tuple(parent[i][j]))

# print(answer)
print(len(answer))