import sys
from collections import deque

input=sys.stdin.readline

dx=[0,0,-1,1]
dy=[-1,1,0,0]

N,M=map(int,input().split())

switchInfo=[[[] for _ in range(N)] for _ in range(N)]
board=[[False]*N for _ in range(N)]
board[0][0]=True
for i in range(M):
    x,y,a,b=map(int,input().split())
    switchInfo[x-1][y-1].append((a-1,b-1))

def bfs(x,y):
    q=deque()
    q.append((x,y))
    visited=[[False]*N for _ in range(N)]
    visited[x][y]=True
    for a,b in switchInfo[x][y]:
        board[a][b]=True
    cnt=1
    while q:
        now=q.popleft()
        for i in range(4):
            nx=now[0]+dx[i]
            ny=now[1]+dy[i]
            if nx<0 or ny<0 or nx>=N or ny>=N:
                continue
            if visited[nx][ny]:
                continue
            if not board[nx][ny]:
                continue
            for x,y in switchInfo[nx][ny]:
                board[x][y]=True
            visited[nx][ny]=True
            q.append((nx,ny))
            cnt+=1
    return cnt

prev=0
while True:
    k=bfs(0,0)
    if k==prev:
        break
    else:
        prev=k

cnt=0
for i in range(N):
    for j in range(N):
        if board[i][j]:
            cnt+=1
print(cnt)