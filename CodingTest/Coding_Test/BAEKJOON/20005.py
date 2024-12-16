import sys
from collections import deque
import heapq

dx=[0,0,-1,1]
dy=[-1,1,0,0]

M,N,P=map(int,input().split())

board=[]
playerPosDict=dict()
playerDpsDict=dict()
bossPos=tuple()
takedTimeToBoss=[[-1]*N for _ in range(M)]
for i in range(M):
    arr=list(input())
    for j in range(N):
        if arr[j]=='B':
            bossPos=(i,j)
            arr[j]='.'
        elif arr[j].isalpha() and arr[j] != 'X':
            playerPosDict[arr[j]]=(i,j)
            arr[j]='.'
    board.append(arr)

for _ in range(P):
    player_num, dps=input().split()
    playerDpsDict[player_num]=int(dps)

bossHP=int(input())

def bfs(x,y):
    global takedTimeToBoss
    q=deque()
    q.append((x,y))
    takedTimeToBoss[x][y]=0
    while q:
        now=q.popleft()
        for i in range(4):
            nx=now[0]+dx[i]
            ny=now[1]+dy[i]
            if nx<0 or ny<0 or nx>=M or ny>=N:
                continue
            if board[nx][ny]=='X':
                continue
            if takedTimeToBoss[nx][ny]!=-1:
                continue
            takedTimeToBoss[nx][ny]=takedTimeToBoss[now[0]][now[1]]+1
            q.append((nx,ny))

bfs(bossPos[0],bossPos[1])
cnt=0
touchedHeapq=[]
for key in playerPosDict.keys():
    x,y=playerPosDict[key]
    heapq.heappush(touchedHeapq,(takedTimeToBoss[x][y],playerDpsDict[key]))

t=0
sumOfDps=0
answer=0
while bossHP>0:
    t+=1
    while touchedHeapq and touchedHeapq[0][0]<=t:
        now=heapq.heappop(touchedHeapq)
        answer+=1
        sumOfDps+=now[1]
    bossHP-=sumOfDps

print(answer)




