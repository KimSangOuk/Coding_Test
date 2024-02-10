# 풀이시간 1시간 20분/1시간 시간제한 1초 메모리제한 1024MB
# 1회차 정답 - But, 풀이시간
# 조건을 놓쳐서 시간이 지연된 문제이다. 다음에는 조건을 적어놓고 놓치는 부분이 있는지 확인하면서 풀어야겠다는 생각이 들었다.
# 풀이의 경우는 BFS이자 시뮬레이션 문제이다. 조건에 따라 연결된 블록 그룹을 BFS를 통해 찾는다. 이때, 우리는 기준에 따라 정렬을 생각하며 정렬조건을 전부 구해내야한다. 그렇게 그룹을 구해낸 다음, 또 그룹 중에서도 기준으로 우리가 원하는 그룹을 찾아낸다. 그런다음 그 그룹을 아래로 내리고 회전시키고 아래로 내리는 작업을 단순 반복하면 된다. 

from collections import deque

n,m=map(int,input().split())

INF=int(1e9)

dx=[0,0,-1,1]
dy=[1,-1,0,0]

board=[]
for _ in range(n):
    board.append(list(map(int,input().split())))

def bfs(x,y,color):
    q=deque()
    q.append((x,y))
    visited=[[False]*n for _ in range(n)]
    visited[x][y]=True
    group_blocks=[]
    total_cnt=0
    rainbow_cnt=0
    while q:
        now=q.popleft()
        if board[now[0]][now[1]]==0:
            group_blocks.append((1,now[0],now[1]))
        else:
            group_blocks.append((0,now[0],now[1]))
        total_cnt+=1
        if board[now[0]][now[1]]==0:
            rainbow_cnt+=1
        for i in range(4):
            nx=now[0]+dx[i]
            ny=now[1]+dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=n:
                continue
            if visited[nx][ny]:
                continue
            if board[nx][ny]==0 or board[nx][ny]==color:
                q.append((nx,ny))
                visited[nx][ny]=True

    if len(group_blocks)<2:
        return False
    group_blocks.sort()
    return [total_cnt,rainbow_cnt,group_blocks[0][1],group_blocks[0][2],group_blocks]

def find_biggest_group(board):
    biggest_cnt=0
    biggest_group=[]
    groups=[]
    for i in range(n):
        for j in range(n):
            if 1<=board[i][j]<INF:
                find_block_group=bfs(i,j,board[i][j])
                if not find_block_group:
                    continue
                groups.append(find_block_group)
    if len(groups)==0:
        return False
    groups.sort(key=lambda x:(-x[0],-x[1],-x[2],-x[3]))
    return groups[0]

def down_block(arr):
    new_arr=[]
    stack=deque()
    floor=n
    for i in range(n-1,-1,-1):
        if 0<=arr[i]<INF:
            stack.append(arr[i])
        if arr[i]==INF:
            continue
        if arr[i]==-1:
            length=len(stack)
            for j in range(length):
                new_arr.append(stack.popleft())
            new_arr+=[INF]*(floor-i-1-length)
            new_arr.append(-1)
            floor=i
    length=len(stack)
    for i in range(length):
        new_arr.append(stack.popleft())
    new_arr+=[INF]*(floor-length)
    return new_arr[::-1]

def gravity_board(board):
    new_board=[[0]*n for _ in range(n)]
    for j in range(n):
        arr=[]
        for i in range(n):
            arr.append(board[i][j])
        arr=down_block(arr)
        for i in range(n):
            new_board[i][j]=arr[i]

    return new_board

def turn_declock_board(board):
    new_board=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new_board[n-j-1][i]=board[i][j]
    return new_board

score=0
while True:
    biggest_group=find_biggest_group(board)
    if not biggest_group:
        print(score)
        break
    total_cnt,all_blocks_of_biggest_group=biggest_group[0],biggest_group[4]

    # 모든 블록 그룹 제거
    score+=total_cnt**2
    for rain_bow_tf,x,y in all_blocks_of_biggest_group:
        board[x][y]=INF

    # 격자 중력
    board=gravity_board(board)

    # 격자 반시계 90도 회전
    board=turn_declock_board(board)

    # 격자 중력
    board=gravity_board(board)