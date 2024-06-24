# 풀이시간 2시간/1시간 시간제한 1초 메모리제한 1024MB
# 1회차 정답 - But, 풀이시간
# 상당히 복잡한 구현, 시뮬레이션 문제이다. 풀이는 문제와 동일하다. 각 구슬을 가져오고 가져온 배열을 다시 넣는 작업을 반복적으로 하므로 함수로 만들어주었다. 

from collections import deque
import copy

n,m=map(int,input().split())

dx=[-1,1,0,0]
dy=[0,0,-1,1]

tdx=[0,1,0,-1]
tdy=[-1,0,1,0]

board=[]
for _ in range(n):
    board.append(list(map(int,input().split())))

start_x,start_y=n//2,n//2

bomb_cnt_marble=[0,0,0]

def blizard(board,d,s,now_x,now_y):
    nx,ny=now_x,now_y
    while s>0:
        nx=nx+dx[d]
        ny=ny+dy[d]
        board[nx][ny]=0
        s-=1

def get_marble_list(board,now_x,now_y):
    q=deque()
    q.append((now_x,now_y,3))
    visited=[[False]*n for _ in range(n)]
    visited[now_x][now_y]=True
    dir=3
    marble_list=[]
    # 구슬 꺼내기
    while q:
        now=q.popleft()
        dir=now[2]
        turn_dir=(dir+1)%4
        tnx=now[0]+tdx[turn_dir]
        tny=now[1]+tdy[turn_dir]
        nx=now[0]+tdx[dir]
        ny=now[1]+tdy[dir]
        if tnx<0 or tny<0 or tnx>=n or tny>=n:
            continue
        if not visited[tnx][tny]:
            visited[tnx][tny]=True
            q.append((tnx,tny,turn_dir))
            if board[tnx][tny]!=0:
                marble_list.append((board[tnx][tny],tnx,tny))
        else:
            if nx<0 or ny<0 or nx>=n or ny>=n:
                break
            if visited[nx][ny]:
                break
            q.append((nx,ny,dir))
            visited[nx][ny]=True
            if board[nx][ny]!=0:
                marble_list.append((board[nx][ny],nx,ny))
    return marble_list

def fill_marble(board,now_x,now_y,marble_list):
    new_board=[[0]*n for _ in range(n)]
    q=deque()
    q.append((now_x,now_y,3))
    visited=[[False]*n for _ in range(n)]
    visited[now_x][now_y]=True
    marble_list=deque(marble_list)
    while q:
        now=q.popleft()
        dir=now[2]
        turn_dir=(dir+1)%4
        tnx=now[0]+tdx[turn_dir]
        tny=now[1]+tdy[turn_dir]
        nx=now[0]+tdx[dir]
        ny=now[1]+tdy[dir]
        if tnx<0 or tny<0 or tnx>=n or tny>=n:
            continue
        if not visited[tnx][tny]:
            visited[tnx][tny]=True
            q.append((tnx,tny,turn_dir))
            new_board[tnx][tny]=marble_list.popleft()
            if len(marble_list)==0:
                break
        else:
            if nx<0 or ny<0 or nx>=n or ny>=n:
                break
            if visited[nx][ny]:
                break
            q.append((nx,ny,dir))
            visited[nx][ny]=True
            new_board[nx][ny]=marble_list.popleft()
            if len(marble_list)==0:
                break
    return new_board

def pick_num_marble_list(marble_list):
    new_list=[]
    for i in range(len(marble_list)):
        new_list.append(marble_list[i][0])
    return new_list

def fill_empty_space(board,now_x,now_y):
    # 빈공간 없앤 후 처음부터 채워넣기
    new_board=[[0]*n for _ in range(n)]
    marble_list=get_marble_list(board,now_x,now_y)
    if len(marble_list)==0:
        return new_board
    new_list=pick_num_marble_list(marble_list)
    new_board=fill_marble(board,now_x,now_y,new_list)
    return new_board

def find_continus_marble(board,start_x,start_y):
    marble_list=get_marble_list(board,start_x,start_y)
    if len(marble_list)==0:
        return marble_list
    result=[]
    cnt=1
    now_num=marble_list[0][0]
    continus_group=[marble_list[0]]
    for i in range(1,len(marble_list)):
        if now_num==board[marble_list[i][1]][marble_list[i][2]]:
            cnt+=1
            continus_group.append(marble_list[i])
        else:
            if cnt>=4:
                result+=continus_group
            continus_group=[marble_list[i]]
            cnt=1
            now_num=board[marble_list[i][1]][marble_list[i][2]]
    if cnt>=4:
        result+=continus_group

    return result

def change_marble(board,start_x,start_y):
    new_board=[[0]*n for _ in range(n)]
    marble_list=get_marble_list(board,start_x,start_y)
    if len(marble_list)==0:
        return new_board
    new_list=[]
    cnt=1
    now_num=marble_list[0][0]
    for i in range(1,len(marble_list)):
        if now_num==board[marble_list[i][1]][marble_list[i][2]]:
            cnt+=1
        else:
            new_list.append(cnt)
            new_list.append(now_num)
            cnt=1
            now_num=board[marble_list[i][1]][marble_list[i][2]]
    if cnt>=1:
        new_list.append(cnt)
        new_list.append(now_num)
    if len(new_list)>n*n-1:
        new_list=new_list[:n*n-1]
    new_board=fill_marble(board,start_x,start_y,new_list)
    return new_board

for blizard_cnt in range(m):
    # 블리자드 명령
    d,s=map(int,input().split())
    d=d-1

    # 상어가 블리자드 시행-> 방향과 거리로 얼음파편으로 구슬 파괴
    blizard(board,d,s,start_x,start_y)

    # 이동과 폭발
    while True:
        board=fill_empty_space(board,start_x,start_y)

        group=find_continus_marble(board,start_x,start_y)
        if len(group)==0:
            break
        for num,x,y in group:
            bomb_cnt_marble[board[x][y]-1]+=1
            board[x][y]=0

    board=change_marble(board,start_x,start_y)


print(bomb_cnt_marble[0]+bomb_cnt_marble[1]*2+bomb_cnt_marble[2]*3)