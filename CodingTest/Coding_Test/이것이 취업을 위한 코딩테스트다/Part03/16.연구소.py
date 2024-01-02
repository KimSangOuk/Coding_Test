# 풀이시간 15분 시간제한 2초 메모리제한 512MB
# 2회차 풀이
# 1회차 풀이 때, 모든 조합을 전부 구해서 푸는 방식을 사용했던 것이 기억나서 벽을 어떻게 세우는지에 따라 풀이 방법이 달라지는 문제인것을 기억해냈다.
# 재귀함수로 벽을 세우는 것을 다루고 있었는데 벽이 세개가 다 세워지면 조건식으로 탐색을 해서 바이러스가 퍼져나가는 방법을 수행하여 답을 구해내고 이닐 경우는 벽을 재귀함수를 통해 다시 벽을 세우고 지우는 것을 반복하는 것이었다.
# 재귀함수가 그래도 많이 익숙해 졌는지 점점 종료조건과 진행하고 다시 돌아온단느 점을 생각해내서 풀어냈다.
# 나머지 부분은 단순 퍼져나가는 부분이라 자세히 쓰지는 않았다.

n,m=map(int,input().split())
board=[]
for i in range(n):
  board.append(list(map(int,input().split())))

def set_case(board):
  if count==3:
    for i in range(n):
      for j in range(m):
        tmp[i][j]=board[i][j]
    for i in range(n):
      for j in range(m):
        if tmp[i][j]==2:
          dfs(i,j)
    for i in range(n):
      for j in range(m):
        if tmp[i][j]==0:
          max_
  else:
    for i in range(n):
      for j in range(m):
        if board[i][j]==0:
          count+=1
          board[i][j]+=1
          set_case(board)
          board[i][j]-=1
          count-=1


# 풀이시간 30분/40분 시간제한 2초 메모리제한 512MB
# 1회차 정답 but 풀이 배울꺼 있다고 판단 -> 한번 더 풀어보기
# 전체적인 데이터의 크기가 가로, 세로 최대 8이기에 64이기 때문에 괜찮으며 여기다가 각 64칸 중 3개씩 고르는 경우가 곱해져도 시간복잡도가 괜찮다고 판단하였다. 브루트 포스(완전 탐색)알고리즘을 사용하면서도 각 경우에 dfs/bfs를 사용하는 알고리즘이라고 생각했다.
# 정답지와의 풀이의 사고 방식은 똑같다. 하지만 표현 방식이 달라서 가져왔다.


# 1회차 풀이
from itertools import combinations
import copy

n,m=map(int,input().split())
board=[]
for _ in range(n):
  board.append(list(map(int,input().split())))

empty_scope=[]
virus_scope=[]

# 나는 조합을 쓰기 위해서 empty_scope를 따로 빼두어 사용했지만 답안지에서는 재귀함수를 사용해서 각 경우를 count로 찾아갔다. 재밌는 방식이라고 생각했다. 그러다가 3개가 맞춰지면 바이러스 경우를 살펴보고 끝나면 리턴해서 함수를 끝내 다시 다른 경우를 탐색한다. 생각해보지 못한 방법이다.
# 바이러스 영역을 따로 찾아둔 이유도 방법이 다르다. 나의 경우는 dfs 함수를 현 지점부터 시작하기 위해 현지점을 기준으로 잡았지만 답안지의 경우는 새로운 방식으로 퍼져나가는 경우를 시작점으로 생각했다. 처음보는 dfs 방식이라고 봐도 무방하고 내가 아직 재귀함수에 익숙하지 않아서 생각해내지 못했다.
for i in range(n):
  for j in range(m):
    if board[i][j]==0:
      empty_scope.append((i,j))
    elif board[i][j]==2:
      virus_scope.append((i,j))
      board[i][j]=0

# 위에서 언급한 조합 방식이다. 답안지에서는 재귀함수로 경우를 탐색한다.
all_case=list(combinations(empty_scope,3))

# 위에서 언급한 시작지점이 현지점인 방식이다. 답안지에서는 현지점이 이미 '2'인점을 감안해서 주변 지점부터 퍼져나가는 것을 택했다.
def dfs(y,x):
  if x<=-1 or x>=m or y<=-1 or y>=n:
    return False
  if new_board[y][x]==0:
    new_board[y][x]=2
    dfs(y-1,x)
    dfs(y,x-1)
    dfs(y+1,x)
    dfs(y,x+1)
    return True
  return False
        
answer=0
for case in all_case:
  # 나는 deepcopy를 사용했으나 답안지에서는 그대로 deepcopy를 구현하는 방식을 택했다.
  new_board=copy.deepcopy(board)
  scope1,scope2,scope3=case
  # print(scope1,scope2,scope3)
  new_board[scope1[0]][scope1[1]]+=1
  new_board[scope2[0]][scope2[1]]+=1
  new_board[scope3[0]][scope3[1]]+=1
  
  for y,x in virus_scope:
    dfs(y,x)

  count=0
  for i in range(n):
    for j in range(m):
      if new_board[i][j]==0:
        count+=1

  answer=max(count,answer)

print(answer)

# 답안지 예시
n,m=map(int,input().split())
board=[] # 초기 맵 리스트
temp=[[0]*m for _ in range(n)] # 벽을 설치한 뒤의 맵 리스트

for _ in range(n):
  board.append(list(map(int,input().split())))

# 4가지 이동 방향에 대한 리스트
dx=[0,-1,0,1]
dy=[-1,0,1,0]

result=0

# 깊이 우선 탐색(DFS)를 이용해 각 바이러스가 사방으로 퍼지도록 하기
def virus(x,y):
  for i in range(4):
    nx=x+dx[i]
    ny=y+dy[i]
    # 상, 하, 좌, 우 중에서 바이러스가 퍼질 수 있는 경우
    if nx>=0 and nx<n and ny>=0 and ny<m:
      if temp[nx][ny]==0:
        # 해당 위치에 바이러스를 배치하고 다시 재귀적으로 수행
        temp[nx][ny]=2
        virus(nx,ny)

# 현재 맵에서 안전 영역의 크기 계산하는 메서드
def get_score():
  score=0
  for i in range(n):
    for j in range(m):
      if temp[i][j]==0:
        score+=1
  return score

# 깊이 우선 탐색(DFS)를 이용해 울타리를 설치하면서, 매번 안전 영역의 크기 계산
def dfs(count):
  global result
  # 울타리가 3개 설치된 경우
  if count==3:
    for i in range(n):
      for j in range(m):
        temp[i][j]=board[i][j]
    # 각 바이러스 위치에서 전파 진행
    for i in range(n):
      for j in range(m):
        if temp[i][j]==2:
          virus(i,j)
    # 안전 영역의 최댓값 계산
    result=max(result,get_score())
    return
  # 빈 공간에 울타리 설치
  for i in range(n):
    for j in range(m):
      if board[i][j]==0:
        board[i][j]=1
        count+=1
        dfs(count)
        board[i][j]=0
        count-=1

dfs(0)
print(result)