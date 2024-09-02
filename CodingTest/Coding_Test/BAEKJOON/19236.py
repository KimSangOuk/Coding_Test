# 풀이시간 3시간 30분/1시간 시간제한 1초 메모리제한 512MB
# 1회차 정답 - but 풀이시간 너무 오래걸림
# 3시간 반동안 오류를 찾느라 오래걸린 문제이다. 풀이방법은 그렇게까지 복잡하지는 않으나, 조건이 까다롭다고 볼 수 있었다. 즉, 시뮬레이션 코딩을 하는데 디테일이 떨어지면 틀릴 수밖에 없는 문제라는 것다.
# 먼저 풀이 방법을 설명하면 물고기의 움직을 나타내는데 방향과 번호가 주어지므로 그것을 4*4 배열에 저장하고 물고기를 일일이 번호순으로 찾아서 조회할 경우 시간이 오래걸리므로 fish에 또 따로 저장해둔다. 이때 물고기의 움직임이 일어나고 상어가 먹이를 찾아 움직이는데 각 움직임 마다 방향이 달라질 가능성이 있고 또, 갈 수 있는 칸이 경우의 수가 달라지기 때문에 경우에 따라 맞춰서 들어가는 DFS문제라고 보고 풀기 시작하였다. 그렇기 때문에 상어의 움직임 부터 보자면 현재의 이동 방향에서 거리는 상관없기 때문에 1씩 늘려가며 움직여보고, 이 때, 움직이는 칸마다 맵에서 벗어나면 더 이상 갈 곳이 없다고 판단하고 while문을 끝내고 빈칸은 가지 못하므로 다음 칸의 경우로 넘어간다. 그렇게 물고기가 있는 칸을 찾으면 그 칸에 있는 물고기를 먹고 방향을 취한다음 DFS로 재귀하여 다음 갈 곳을 찾는다. 이 각 경우에 따라 물고기의 이동도 일어나기 때문에 상어 이동전에 물고기 이동을 하는 것을 넣어주면 된다. 물고기의 이동 같은 경우 각 순서대로 물고기를 찾는데 물고기가 없을 경우는 지나치고 있을 경우에만 벽과 상어가 아닌 방향을 찾아서 반시계 방향대로 움직여주다가 움직이려는 칸에 물고기가 있다면 그 물고기와 자리를 바꾸고 빈칸이라면 그냥 이동하면 된다.
# 시간이 크게 지연되고 찾기 어려웠던 3가지 원인이 있는데 하나씩 따져보겠다.
# 첫번째는 물고기가 이동하기 전에 물고기의 방향을 수정해놓고 board를 업데이트 했어야 했는데 이를 놓쳤다. 특정 값이 바뀌고 나서 교환이 되는가를 확인했어야 하는 문제였는데 다음부터는 교환이나 특정 조건이 일어날 때, 그 작동이 되기 전의 값이 우리가 원하는대로 반영이 되었는지를 확인할 필요가 있다고 생각이 든다.
# 두 번째는 크게 깨달음을 얻었는데, 배열과 같이 주소 값이 함수로 넘어가는 경우에는 dfs 상에서 분리된 상태가 아닌 하나의 상태로 이어질 수 있다는 것이다. 이 부분을 지식은 알고 있었으나 실전에서는 처음 느껴보는 것이라 찾기 매우 어려웠다. 
# 세 번재는 단순히 방향을 움직이는데 문제였다. 방향을 한칸씩 이동시켜야 하는데 여러칸씩 이동시키고 있었고 이렇게 여러칸씩 이동시키는데 찾지 못했던 이유는 예비 값이 아닌 직접 반영한 값을 쓰고 있었기 때문이다. 습관적으로 예비 값이 아니더라도 그저 1 올라간다고 판단했던거 같다.

import copy

dx=[-1,-1,0,1,1,1,0,-1]
dy=[0,-1,-1,-1,0,1,1,1]

board=[[[] for _ in range(4)] for _ in range(4)]
fish=dict()
for i in range(4):
    arr=list(map(int,input().split()))
    for j in range(0,8,2):
        board[i][j//2].append(arr[j])
        board[i][j//2].append(arr[j+1]-1)
        fish[arr[j]]=[i,j//2,arr[j+1]-1]


def dfs(board_tmp,fish_tmp,x,y,d,value):
    board=copy.deepcopy(board_tmp) # 2번 시간 지연 원인
    fish=copy.deepcopy(fish_tmp)

    global result
    for i in range(1,17):
        if fish[i]==0:
            continue
        fx,fy,fd=fish[i]
        find=False
        for k in range(8):
            nd=(fd+k)%8 # 3번 시간 지연 원인
            nx=fx+dx[nd]
            ny=fy+dy[nd]
            if nx<0 or ny<0 or nx>=4 or ny>=4:
                continue
            if nx==x and ny==y:
                continue
            find=True
            nx=fx+dx[nd]
            ny=fy+dy[nd]
            board[fx][fy][1]=nd # 1번 시간지연 원인
            fish[i]=[nx,ny,nd]
            if len(board[nx][ny])>0:
                fish[board[nx][ny][0]]=[fx,fy,board[nx][ny][1]]
            board[nx][ny],board[fx][fy]=board[fx][fy],board[nx][ny]
            break
    k=0
    while True:
        k+=1
        nx=x+k*dx[d]
        ny=y+k*dy[d]
        if nx<0 or ny<0 or nx>=4 or ny>=4:
            break
        if len(board[nx][ny])==0:
            continue
        result=max(result,value+board[nx][ny][0])
        tmp_num,tmp_dir=board[nx][ny]
        fish[tmp_num]=0
        board[nx][ny]=[]
        dfs(board,fish,nx,ny,tmp_dir,value+tmp_num)
        board[nx][ny]=[tmp_num,tmp_dir]
        fish[tmp_num]=[nx,ny,tmp_dir]

result=0
x,y=0,0
d=board[0][0][1]
fish[board[0][0][0]]=0
value=board[0][0][0]
board[0][0]=[]

dfs(board,fish,x,y,d,value)
print(result)


# 배운 점
# 함수를 사용하므로써 변수의 중복 문제와 범위 문제에서 벗어날 수 있다는 점에 풀이를 간략화 할 수 있다는 점을 새삼 깨달았다. 또한, 상어가 물고기의 방향으로 이동하더라도 빈칸으로는 가지 못하기 때문에 그 방향으로 갔을 때의 물고기의 방향을 그대로 사용해야 되어서 따로 방향을 기록할 필요가 없기도 하고 또한 물고기를 따로 기록할 필요 없다는 점 또한 깨달았다. 즉, 기록적인 면에서 물고기의 방향을 따라간다는 것을 인지하고 기록을 생각했다면 더 좋았을 것이다. 또한 물고기를 따로 안하고 위치를 매번 불러왔는데 이 것도 시간복잡도가 괜찮다는 전제 조건하에서 가능했다는 것이므로 시간복잡도를 확인하였다면 따로 물고기의 위치를 기록해둘 필요는 없었을 것이다. 그리고 메인 흐름의 함수를 짤때, 처음의 경우를 포함할 수 있도록 짜는 것을 확인하고 짜는 것이 좋다는 생각이 들었다. 또한 무지성으로 max의 값을 찾는 방법보다는 확실히 방버이 없을 경우 max하고 return 할 수 잇는 방법을 찾는 것이 더 좋아보인다. 이 문제에서의 경우에는 상어가 갈 수 있는 방법을 전부 탐색하고 그 모든 경우에 관해서 탐색을 돌리면 되기 때문에 굳이 연결시키지 않고 따로 구한다음 방법이 없다면 max하고 return 하면 되었을 것이다.
# 답안지
import copy

# 4*4 크기의 정사각형에 존재하는 각 물고기의 번호(없으면 -1)와 방향 값을 담는 테이블

for i in range(4):
  data=list(map(int,input().split()))
  # 매 줄마다 4마리의 물고기를 하나씩 확인하며
  for j in range(4):
    # 각 위치마다 [물고기의 번호, 방향]을 저장
    array[i][j]=[data[j*2],data[j*2+1]-1]

# 8가지 방향에 대한 정의
dx=[-1,-1,0,1,1,1,0,-1]
dy=[0,-1,-1,-1,0,1,1,1]

# 현재 위치에서 왼쪽으로 회전된 결과 반환
def turn_left(direction):
  return (direction+1)%8

result = 0 # 최종 결과

# 현재 배열에서 특정한 번호의 물고기 위치 찾기
def find_fish(array,index):
  for i in range(4):
    for j in range(4):
      if array[i][j][0]==index:
        return (i,j)
  return None

# 모든 물고기를 회전 및 이동시키는 함수
def move_all_fishes(array,now_x,now_y):
  # 1번부터 16번까지의 물고기를 차례대로 (낮은 번호부터) 확인
  for i in range(1,17):
    # 해당 물고기의 위치 찾기
    position=find_fish(array,i)
    if position!=None:
      x,y=position[0],position[1]
      direction=array[x][y][1]
      # 해당 물고기의 방향을 왼쪽으로 계속 회전시키며 이동이 가능한지 확인
      for j in range(8):
        nx=x+dx[direction]
        ny=y+dy[direction]
        # 해당 방향으로 이동이 가능하다면 이동시키기
        if 0<=nx and nx<4 and 0<=ny and ny<4:
          if not (nx==now_x and ny==now_y):
            array[x][y][1]=direction
            array[x][y],array[nx][ny]=array[nx][ny],array[x][y]
            break
        direction=turn_left(direction)

# 상어가 현재 위치에서 먹을 수 있는 모든 물고기의 위치 반환
def get_possible_position(array,now_x,now_y):
  positions=[]
  direction=array[now_x][now_y][1]
  # 현재의 방향으로 계속 이동시키기
  for i in range(4):
    now_x+=dx[direction]
    now_y+=dy[direction]
    # 범위를 벗어나지 않는지 확인하며
    if 0<=now_x and now_x<4 and 0<=now_y and now_y<4:
      # 물고기가 존재하는 경우
      if array[now_x][now_y][0]!=-1:
        positions.append((now_x,now_y))
  return positions

# 모든 경우를 탐색하기 위한 DFS 함수
def dfs(array,now_x,now_y,total):
  global result
  array=copy.deepcopy(array) # 리스트를 통째로 복사

  total+=array[now_x][now_y][0] # 현재 위치의 물고기 먹기
  array[now_x][now_y][0]=-1 # 물고기를 먹었으므로 번호 값을 -1로 변환

  move_all_fishes(array,now_x,now_y) # 전체 물고기 이동시키기

  # 이제 다시 상어가 이동할 차례이므로, 이동가능한 위치 찾기
  possible_position=get_possible_position(array,now_x,now_y)
  # 이동할 수 있는 위치가 하나도 없다면 종료
  if len(possible_position)==0:
    result=max(result,total)
    return
  # 모든 이동할 수 있는 위치로 재귀적으로 수행
  for next_x,next_y in positions:
    dfs(array,next_x,next_y,total)

# 청소년 상어의 시작 위치(0,0)에서부터 재귀적으로 모든 경우 탐색





import copy
fishes=dict()
board=[[0]*4 for _ in range(4)]
for i in range(4):
    arr=list(map(int,input().split()))
    for j in range(0,2*4,2):
        a,b=arr[j],arr[j+1]
        board[i][j//2]=a
        fishes[a]=[i,j//2,b-1]

dx=[-1,-1,0,1,1,1,0,-1]
dy=[0,-1,-1,-1,0,1,1,1]

shark=[0,0,0]
score=board[0][0]
shark[2]=fishes[board[0][0]][2]
del fishes[board[0][0]]
board[0][0]=-1
answer=0

def moveFish(fishes,board,shark):
    for fishNum in sorted(fishes.keys()):
        x,y,d=fishes[fishNum]
        for i in range(8):
            nx=x+dx[(d+i)%8]
            ny=y+dy[(d+i)%8]
            if nx<0 or ny<0 or nx>=4 or ny>=4:
                continue
            if shark[0]==nx and shark[1]==ny:
                continue
            if board[nx][ny]!=-1:
                fishes[board[nx][ny]][0]=x
                fishes[board[nx][ny]][1]=y
            fishes[fishNum]=[nx,ny,(d+i)%8]
            board[nx][ny],board[x][y]=board[x][y],board[nx][ny]
            break


def dfs(score,shark,newBoard,newFishes):
    global answer
    moveFish(newFishes,newBoard,shark)
    t=1
    while True:
        nx=shark[0]+dx[shark[2]]*t
        ny=shark[1]+dy[shark[2]]*t
        if nx<0 or ny<0 or nx>=4 or ny>=4:
            answer=max(answer,score)
            return
        if newBoard[nx][ny]==-1:
            t+=1
            continue
        board=copy.deepcopy(newBoard)
        fishes=copy.deepcopy(newFishes)
        tmpNum=board[nx][ny]
        tmpFish=fishes[tmpNum]
        board[nx][ny]=-1
        del fishes[tmpNum]
        dfs(score+tmpNum,[nx,ny,tmpFish[2]],board,fishes)
        t+=1

dfs(score,shark,board,fishes)
print(answer)