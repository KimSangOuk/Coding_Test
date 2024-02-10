# 풀이시간 30분 시간제한 2초 메모리제한 1024MB
# 1회차 정답
# 주사위의 회전에 따른 이동을 나타내고 그 이동에 따라 점수를 구해서 합산하는 문제이다. 주사위는 2차원 배열로 가로와 세로로 표현하여 회전시킬 때, 위 아래를 유지시키며 회전을 표현할 수 있으며 더 이상 갈 칸이 없을 때는 방향을 바꿔주면 된다. 또한 점수를 구할 때는 현재의 칸에 숫자에 따라 BFS를 수행해주면 된다. 마지막으로 그 칸의 숫자와 주사위의 아랫칸에 따라 방향을 시계 또는 반시계로 바꿔주면서 K번 반복 실행해주면 된다.

from collections import deque

n,m,k=map(int,input().split())

dx=[0,1,0,-1]
dy=[1,0,-1,0]

board=[]
for _ in range(n):
    board.append(list(map(int,input().split())))

def move_dice(dice,dir):
    if dir==0:
        dice[0].appendleft(dice[0].pop())
        dice[1][0],dice[1][2]=dice[0][0],dice[0][2]
    if dir==2:
        dice[0].append(dice[0].popleft())
        dice[1][0],dice[1][2]=dice[0][0],dice[0][2]
    if dir==1:
        dice[1].appendleft(dice[1].pop())
        dice[0][0],dice[0][2]=dice[1][0],dice[1][2]
    if dir==3:
        dice[1].append(dice[1].popleft())
        dice[0][0],dice[0][2]=dice[1][0],dice[1][2]

def get_score(board,x,y):
    B=board[x][y]
    count=0
    q=deque()
    q.append((x,y))
    visited=[[False]*m for _ in range(n)]
    visited[x][y]=True
    while q:
        count+=1
        now_x,now_y=q.popleft()
        for i in range(4):
            nx=now_x+dx[i]
            ny=now_y+dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=m or visited[nx][ny]:
                continue
            if board[nx][ny]!=B:
                continue
            visited[nx][ny]=True
            q.append((nx,ny))
    return count*B

dice=[deque([1,3,6,4]),deque([1,5,6,2])]
dir=0
x,y=0,0
score=0
while k>0:
    k-=1
    nx=x+dx[dir]
    ny=y+dy[dir]
    if nx<0 or ny<0 or nx>=n or ny>=m:
        dir=(dir+2)%4
        nx=x+dx[dir]
        ny=y+dy[dir]
    x,y=nx,ny
    move_dice(dice,dir)

    score+=get_score(board,x,y)

    A=dice[0][2]
    B=board[x][y]
    if A>B:
        dir=(dir+1)%4
    elif A<B:
        dir=(dir-1)%4

print(score)