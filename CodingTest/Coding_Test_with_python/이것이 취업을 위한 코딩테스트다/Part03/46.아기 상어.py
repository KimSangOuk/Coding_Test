# 풀이시간 33분/50분 시간제한 2초 메모리제한 512MB
# 2회차 정답
# 단순히 주어진 풀이대로 푸는 시뮬레이션 유형에 물고기를 찾을 때, 탐색을 쓰는 문제 나같은 경우는 bfs를 사용했다. 전체 맵의 크기가 400칸이고 물고기로 꽉차있어서 전부 탐색해야 한다해도 160,000번 연산 횟수로 가능한 문제이다.

from collections import deque

dx=[0,0,1,-1]
dy=[1,-1,0,0]

n=int(input())

pos_babyShark=[0,0]
size_babyShark=2
board=[]
for i in range(n):
    arr=list(map(int,input().split()))
    for j in range(n):
        if arr[j]==9:
            pos_babyShark[0]=i
            pos_babyShark[1]=j
    board.append(arr)
board[pos_babyShark[0]][pos_babyShark[1]]=0

def bfs(start):
    visited=[[-1]*n for _ in range(n)]
    q=deque()
    q.append(start)
    visited[start[0]][start[1]]=0
    fishes=[]
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=n or visited[nx][ny]>-1:
                continue
            if board[nx][ny]>size_babyShark:
                continue
            visited[nx][ny]=visited[x][y]+1
            q.append((nx,ny))
            if 0<board[nx][ny]<size_babyShark:
                fishes.append((visited[nx][ny],nx,ny))
    return fishes

t=0
eat_count=0
while True:
    # 먹을 물고기가 있는지 탐색
    fishes=bfs(pos_babyShark)

    # 아기 상어가 더 이상 먹을 것이 없으면 종료
    if len(fishes)==0:
        break

    # 먹을 물고기 탐색, 가장 가깝고 위에, 왼쪽
    fishes.sort(key=lambda x:(x[0],x[1],x[2]))
    now_eat_fish=fishes[0]

    # 물고기 먹고 그 자리로 이동
    eat_count+=1
    pos_babyShark[0]=now_eat_fish[1]
    pos_babyShark[1]=now_eat_fish[2]
    board[now_eat_fish[1]][now_eat_fish[2]]=0

    if eat_count==size_babyShark:
        size_babyShark+=1
        eat_count=0

    # 1초 지남
    t+=now_eat_fish[0]

print(t)

# 풀이시간 1시간 20분/50분 시간제한 2초 메모리제한 512MB
# 1회차 정답 - 풀이시간이 오래 걸림
# 단순하게 보드에서 상어 위치를 지워주지 않아 경로 거리를 재는데 오류가 생겨 오래 걸렸다. 이거 찾는데만 30분 넘게 썼다.
# 문제 자체는 주어진 조건을 그대로 코드로 구현해 나가는 시뮬레이션 유형에 현재 위치에서 물고기를 탐색해야 하는 BFS 문제이다.

from collections import deque

# 공간의 크기
n=int(input())
board=[] # 공간

dx=[0,0,1,-1]
dy=[1,-1,0,0]

shark_pos=[0,0] # 상어의 위치
shark_size=2 # 상어의 처음 크기
fish_num=0 # 물고기의 개수
eat_fish=0 # 먹은 물고기의 수
# 공간의 지도 받아오기
for i in range(n):
  arr=list(map(int,input().split()))
  for j in range(n):
    # 상어의 처음 위치
    if arr[j]==9:
      shark_pos=[i,j]
    elif 1<=arr[j]<=6:
      fish_num+=1
  board.append(arr)

board[shark_pos[0]][shark_pos[1]]=0

def dfs(start):
  q=deque()
  q.append(start)
  fishes=[]
  dist_map=[[-1]*n for _ in range(n)]
  dist_map[start[0]][start[1]]=0
  while q:
    x,y=q.popleft()
    for i in range(4):
      nx=x+dx[i]
      ny=y+dy[i]
      if nx<0 or nx>=n or ny<0 or ny>=n or dist_map[nx][ny]!=-1:
        continue
      if board[nx][ny]>shark_size:
        continue
      q.append((nx,ny))
      dist_map[nx][ny]=dist_map[x][y]+1
      if 1<=board[nx][ny]<shark_size:
        fishes.append((dist_map[nx][ny],nx,ny))
  return fishes

time=0 # 걸리는 시간
while True:
  # 전부다 물고기를 먹어서 물고기 없을 경우 엄마 상어에게 도움 호출
  if fish_num==0:
    break
  
  fishes=dfs(shark_pos) # 현 위치 기준으로 물고기 찾기
  # 물고기를 탐색했는데 현재 사이즈에서 먹을 수 있는 물고기가 없거나 도달할 수 있는 물고기가 없는 경우, 엄마 상어에게 도움 호출
  if len(fishes)==0:
    break
  # print(fishes)
  fishes.sort() # 물고기 중 가장 가깝고, 가까운 것중에 제일 위에 있고, 제일 위에 있는 것중 왼쪽
  # print(fishes)
  dist,x,y=fishes[0]

  # 물고기가 있는 곳까지 이동 / 식사
  time+=dist
  shark_pos=[x,y]
  fish_num-=1
  board[x][y]=0

  eat_fish+=1
  # 만약 먹은 물고기의 수가 상어의 크기만큼이면 사이즈 업하고 먹은 물고기 수 초기화
  if eat_fish==shark_size:
    eat_fish=0
    shark_size+=1
  

print(time)