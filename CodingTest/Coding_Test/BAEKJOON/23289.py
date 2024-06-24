# 풀이시간 2시간 시간제한 2초 메모리제한 1024MB
# 1회차 정답 - But, 풀이시간 초과
# 구현, 시뮬레이션 고난이도 유형이다. 단계별로 차례로 구현해가면서 풀면 된다.
# 모든 온풍기를 방향별로 저장해두고 1번 과정에서는 이를 전부 불러 온다. 각 바람은 영향을 줄 수 있기 때문에 동시 진행하기 위해서 따로 배열을 두고 진행한 다음 합친다. 각 진행을 할 때, 경계와 벽을 유의하면서 진행 안한 곳으로 3곳으로 향한다. 벽의 경우는 따로 함수를 두어 확인가능하게 만든다. 모든 경우를 통과한 바람은 1씩 줄어들며 확산되며 0이 되는 경우는 굳이 퍼지지 않게 한다.
# 2번 과정에서는 모든 쌍을 확인하며 벽이 없는 인접한 칸들에서 온도 조절이 일어난다. 방문했던 쌍은 다시 방문하지 않게 하며 이 또한 동시진행이기 때문에 따로 값을 빼두었다가 최종결과에 더하게 한다.
# 3번 과정에서는 단순히 외곽에서 1보다 크거나 같은 온도들에서 1을 빼준다.
# 4번 과정에서는 초콜릿을 먹고
# 5번에서는 조사하는 칸의 온도를 확인하여 종료여부를 결정하도록 한다.

from collections import deque

r,c,k=map(int,input().split())

dx=[0,0,-1,1]
dy=[1,-1,0,0]

board=[[0]*c for _ in range(r)]
check_block=[]
heater=dict()
for i in range(1,5):
    heater[i]=[]
for i in range(r):
    arr=list(map(int,input().split()))
    for j in range(c):
        if 1<=arr[j]<=4:
            heater[arr[j]].append((i,j))
        elif arr[j]==5:
            check_block.append((i,j))

wall=set()
w=int(input())
for i in range(w):
    x,y,t=map(int,input().split())
    wall.add((x-1,y-1,t))

def turn_left(dir):
    if dir==0:
        return 2
    if dir==1:
        return 3
    if dir==2:
        return 1
    if dir==3:
        return 0

def turn_right(dir):
    if dir==0:
        return 3
    if dir==1:
        return 2
    if dir==2:
        return 0
    if dir==3:
        return 1

def blow_heater_wind(tmp,start_x,start_y,dir):
    q=deque()
    tmp[start_x+dx[dir]][start_y+dy[dir]]=5
    q.append((start_x+dx[dir],start_y+dy[dir],5))
    while q:
        now=q.popleft()
        if now[2]-1==0:
            break
        dir_left=turn_left(dir)
        dir_right=turn_right(dir)
        pos1_x,pos1_y=now[0]+dx[dir],now[1]+dy[dir]
        pos2_x,pos2_y=now[0]+dx[dir]+dx[dir_left],now[1]+dy[dir]+dy[dir_left]
        pos3_x,pos3_y=now[0]+dx[dir]+dx[dir_right],now[1]+dy[dir]+dy[dir_right]
        if 0<=pos1_x<r and 0<=pos1_y<c:
            if tmp[pos1_x][pos1_y]==0:
                if not check_wall((now[0],now[1]),(pos1_x,pos1_y)):
                    tmp[pos1_x][pos1_y]=now[2]-1
                    q.append((pos1_x,pos1_y,now[2]-1))
        if 0<=pos2_x<r and 0<=pos2_y<c:
            if tmp[pos2_x][pos2_y]==0:
                tmp_block_x,tmp_block_y=now[0]+dx[dir_left],now[1]+dy[dir_left]
                if not check_wall((tmp_block_x,tmp_block_y),(now[0],now[1])):
                    if not check_wall((tmp_block_x,tmp_block_y),(pos2_x,pos2_y)):
                        tmp[pos2_x][pos2_y]=now[2]-1
                        q.append((pos2_x,pos2_y,now[2]-1))
        if 0<=pos3_x<r and 0<=pos3_y<c:
            if tmp[pos3_x][pos3_y]==0:
                tmp_block_x,tmp_block_y=now[0]+dx[dir_right],now[1]+dy[dir_right]
                if not check_wall((tmp_block_x,tmp_block_y),(now[0],now[1])):
                    if not check_wall((tmp_block_x,tmp_block_y),(pos3_x,pos3_y)):
                        tmp[pos3_x][pos3_y]=now[2]-1
                        q.append((pos3_x,pos3_y,now[2]-1))


def heater_wind_on(board):
    wind_tmp=[[0]*c for _ in range(r)]
    for i in range(1,5):
        direction=i-1
        for x,y in heater[i]:
            tmp=[[0]*c for _ in range(r)]
            blow_heater_wind(tmp,x,y,direction)
            for n in range(r):
                for m in range(c):
                    wind_tmp[n][m]+=tmp[n][m]
    for i in range(r):
        for j in range(c):
            board[i][j]+=wind_tmp[i][j]

def check_wall(pos1,pos2):
    if pos1[0]==pos2[0]:
        if pos1[1]<pos2[1]:
            if (pos1[0],pos1[1],1) in wall:
                return True
        if pos1[1]>pos2[1]:
            if (pos2[0],pos2[1],1) in wall:
                return True
    elif pos1[1]==pos2[1]:
        if pos1[0]>pos2[0]:
            if (pos1[0],pos1[1],0) in wall:
                return True
        if pos1[0]<pos2[0]:
            if (pos2[0],pos2[1],0) in wall:
                return True
    return False

def control_temperature(board):
    up_down_tmp=[[0]*c for _ in range(r)]
    visited=set()
    for i in range(r):
        for j in range(c):
            now_block_pos=(i,j)
            for k in range(4):
                nx=now_block_pos[0]+dx[k]
                ny=now_block_pos[1]+dy[k]
                if nx<0 or ny<0 or nx>=r or ny>=c:
                    continue
                case=[now_block_pos,(nx,ny)]
                case.sort()
                case=tuple(case)
                if case in visited:
                    continue
                visited.add(case)
                if check_wall(now_block_pos,(nx,ny)):
                    continue
                value=abs(board[nx][ny]-board[now_block_pos[0]][now_block_pos[1]])//4
                if board[nx][ny]<board[now_block_pos[0]][now_block_pos[1]]:
                    up_down_tmp[nx][ny]+=value
                    up_down_tmp[now_block_pos[0]][now_block_pos[1]]-=value
                elif board[nx][ny]>board[now_block_pos[0]][now_block_pos[1]]:
                    up_down_tmp[nx][ny]-=value
                    up_down_tmp[now_block_pos[0]][now_block_pos[1]]+=value
    for i in range(r):
        for j in range(c):
            board[i][j]+=up_down_tmp[i][j]

def decrease_border_temperature(board):
    for i in range(r):
        for j in range(c):
            if i==0 or i==r-1 or j==0 or j==c-1:
                if board[i][j]>=1:
                    board[i][j]-=1

def check_all_check_block(board,check_block):
    for x,y in check_block:
        if board[x][y]<k:
            return False
    return True

chocolate=0
while chocolate<=100:

    # 1. 집에 있는 모든 온풍기 바람 1회
    heater_wind_on(board)

    # 2. 온도 조절
    control_temperature(board)

    # 3. 온도가 1 이상인 가장 바깥쪽 온도가 1씩 감소
    decrease_border_temperature(board)

    # 4. 초콜렛을 하나 섭취한다.
    chocolate+=1

    #5. 조사하는 모든 칸의 온도가 K이상인지 검사
    if check_all_check_block(board,check_block):
        break

print(chocolate)