import sys
from collections import deque

input=sys.stdin.readline

dx=[0,0,-1,1]
dy=[-1,1,0,0]

N=int(input())

board=[list(map(int,input().split())) for _ in range(N)]

islandCheckBoard=[[-1]*N for _ in range(N)]

islandBlocksDict=dict()

def findIslandBfs(x,y,num):
    q=deque()
    q.append((x,y))
    islandCheckBoard[x][y]=num
    setBlocks=set()
    setBlocks.add((x,y))
    while q:
        now=q.popleft()
        for i in range(4):
            nx=now[0]+dx[i]
            ny=now[1]+dy[i]
            if nx<0 or ny<0 or nx>=N or ny>=N:
                continue
            if board[nx][ny]==0:
                continue
            if islandCheckBoard[nx][ny]>0:
                continue
            q.append((nx,ny))
            islandCheckBoard[nx][ny]=num
            setBlocks.add((nx,ny))
    return setBlocks

cnt=0
for i in range(N):
    for j in range(N):
        if board[i][j]==1 and islandCheckBoard[i][j]==-1:
            cnt+=1
            islandBlocksDict[cnt]=findIslandBfs(i,j,cnt)

answer=1e9
for key in islandBlocksDict.keys():
    visited=[[-1]*N for _ in range(N)]
    q=deque()
    for x,y in islandBlocksDict[key]:
        visited[x][y]=0
        q.append((x,y))
    thisMin=1e9
    while q:
        finded=False
        now=q.popleft()
        for i in range(4):
            nx=now[0]+dx[i]
            ny=now[1]+dy[i]
            if nx<0 or ny<0 or nx>=N or ny>=N:
                continue
            if visited[nx][ny]>=0:
                continue
            if board[nx][ny]==1:
                thisMin=min(visited[now[0]][now[1]],thisMin)
                finded=True
            else:
                q.append((nx,ny))
                visited[nx][ny]=visited[now[0]][now[1]]+1
        if finded:
            break
    answer=min(thisMin,answer)
print(answer)

