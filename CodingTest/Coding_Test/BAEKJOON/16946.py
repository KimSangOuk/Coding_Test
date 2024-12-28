import sys
from collections import deque

input=sys.stdin.readline

dx=[0,0,-1,1]
dy=[-1,1,0,0]

N,M=map(int,input().split())

board=[list(map(int,list(input().strip()))) for _ in range(N)]

tagBoard=[[0]*M for _ in range(N)]

answer=[[0]*M for _ in range(N)]

def bfs(x,y):
    global board, tagBoard,zeroVisited
    q=deque()
    q.append((x,y))
    blocks=[(x,y)]
    cnt=1
    zeroVisited[x][y]=True
    while q:
        now=q.popleft()
        for i in range(4):
            nx=now[0]+dx[i]
            ny=now[1]+dy[i]
            if nx<0 or ny<0 or nx>=N or ny>=M:
                continue
            if zeroVisited[nx][ny]:
                continue
            if board[nx][ny]==1:
                continue
            q.append((nx,ny))
            zeroVisited[nx][ny]=True
            cnt+=1
            blocks.append((nx,ny))
    for i,j in blocks:
        tagBoard[i][j]=(cnt,x,y)

zeroVisited=[[False]*M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if board[i][j]==0 and not zeroVisited[i][j]:
            bfs(i,j)

for i in range(N):
    for j in range(M):
        if board[i][j]==1:
            cnt=1
            visited=set()
            for k in range(4):
                nx=i+dx[k]
                ny=j+dy[k]
                if nx<0 or ny<0 or nx>=N or ny>=M:
                    continue
                if board[nx][ny]==1:
                    continue
                if (tagBoard[nx][ny][1],tagBoard[nx][ny][2]) in visited:
                    continue
                cnt+=tagBoard[nx][ny][0]
                visited.add((tagBoard[nx][ny][1],tagBoard[nx][ny][2]))
            answer[i][j]=cnt%10

for i in range(N):
    print("".join(map(str,answer[i])))