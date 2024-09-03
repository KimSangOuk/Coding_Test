import sys
from collections import deque
input=sys.stdin.readline

dx=[0,0,-1,1]
dy=[-1,1,0,0]
hdx=[-2,-1,1,2,2,1,-1,-2]
hdy=[1,2,2,1,-1,-2,-2,-1]

K=int(input())
W,H=map(int,input().split())
board=[list(map(int,input().split())) for _ in range(H)]

visited=[[[-1]*W for _ in range(H)] for _ in range(K+1)]
q=deque()
q.append((0,0,K))
visited[K][0][0]=0

while q:
    x,y,leftK=q.popleft()
    if leftK>0:
        for i in range(8):
            nx=x+hdx[i]
            ny=y+hdy[i]
            if nx<0 or ny<0 or nx>=H or ny>=W:
                continue
            if visited[leftK-1][nx][ny]!=-1:
                continue
            if board[nx][ny]==1:
                continue
            visited[leftK-1][nx][ny]=visited[leftK][x][y]+1
            q.append((nx,ny,leftK-1))
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx<0 or ny<0 or nx>=H or ny>=W:
            continue
        if visited[leftK][nx][ny]!=-1:
            continue
        if board[nx][ny]==1:
            continue
        visited[leftK][nx][ny]=visited[leftK][x][y]+1
        q.append((nx,ny,leftK))

answer=40001
for i in range(K+1):
    if visited[i][H-1][W-1]!=-1:
        answer=min(answer,visited[i][H-1][W-1])
if answer==40001:
    print(-1)
else:
    print(answer)