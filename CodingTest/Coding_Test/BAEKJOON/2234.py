import sys
from collections import deque

dx=[0,-1,0,1]
dy=[-1,0,1,0]

input=sys.stdin.readline

N,M=map(int,input().split())

board=[]
for _ in range(M):
    arr=list(map(int,input().split()))
    board.append(arr)

visited=[[False]*N for _ in range(M)]
roomDict=dict()

def bfs(x,y):
    global visited, largestRoomSize, roomDict, roomCnt
    q=deque()
    thisRoomBlocks=[]
    thisRoomBlocks.append((x,y))
    q.append((x,y))
    visited[x][y]=True
    thisRoomSize=1
    while q:
        now=q.popleft()
        for i in range(4):
            nx=now[0]+dx[i]
            ny=now[1]+dy[i]
            if nx<0 or ny<0 or nx>=M or ny>=N:
                continue
            if board[now[0]][now[1]]&(1<<i):
                continue
            if visited[nx][ny]:
                continue
            visited[nx][ny]=True
            q.append((nx,ny))
            thisRoomBlocks.append((nx,ny))
            thisRoomSize+=1
    roomDict[roomCnt]=thisRoomBlocks
    largestRoomSize=max(largestRoomSize,thisRoomSize)


roomCnt=0
largestRoomSize=0
for i in range(M):
    for j in range(N):
        if not visited[i][j]:
            bfs(i,j)
            roomCnt+=1

sumOfLargestTwoRoomSize=0

for i in range(roomCnt-1):
    for j in range(i+1,roomCnt):
        for x1,y1 in roomDict[i]:
            enabled=False
            for x2,y2 in roomDict[j]:
                if (abs(x1-x2)==1 and abs(y1-y2)==0) or (abs(y1-y2)==1 and abs(x1-x2)==0):
                    enabled=True
                    sumOfLargestTwoRoomSize=max(sumOfLargestTwoRoomSize,len(roomDict[i])+len(roomDict[j]))
                    break
            if enabled:
                break

print(roomCnt)
print(largestRoomSize)
print(sumOfLargestTwoRoomSize)