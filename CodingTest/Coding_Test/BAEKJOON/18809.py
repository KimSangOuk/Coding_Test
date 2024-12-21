import sys
from itertools import combinations
from collections import deque

dx=[0,0,-1,1]
dy=[-1,1,0,0]

input=sys.stdin.readline

N,M,G,R=map(int,input().split())

board=[]
enabled=[]
for i in range(N):
    arr=list(map(int,input().split()))
    for j in range(M):
        if arr[j]==2:
            enabled.append((i,j))
    board.append(arr)

def bfs(case_g,case_r):
    global board
    visited=[[['N',-1] for _ in range(M)] for _ in range(N)]
    q=deque()
    numOfFlowers=0
    for x,y in case_g:
        visited[x][y][0]='G'
        visited[x][y][1]=0
        q.append((x,y,'G'))
    for x,y in case_r:
        visited[x][y][0]='R'
        visited[x][y][1]=0
        q.append((x,y,'R'))
    while q:
        now=q.popleft()
        if visited[now[0]][now[1]][0]=='F':
            continue
        for i in range(4):
            nx=now[0]+dx[i]
            ny=now[1]+dy[i]
            if nx<0 or ny<0 or nx>=N or ny>=M:
                continue
            if board[nx][ny]==0:
                continue
            if visited[nx][ny][0]==now[2]:
                continue
            if visited[nx][ny][0]=='F':
                continue
            if visited[nx][ny][0]=='N':
                visited[nx][ny][0]=now[2]
                visited[nx][ny][1]=visited[now[0]][now[1]][1]+1
                q.append((nx,ny,now[2]))
            elif visited[nx][ny][0]!=now[2]:
                if visited[nx][ny][1]!=visited[now[0]][now[1]][1]+1:
                    continue
                visited[nx][ny][0]='F'
                numOfFlowers+=1
                visited[nx][ny][1]=visited[now[0]][now[1]][1]+1
    return numOfFlowers
answer=0
for case_g in list(combinations(enabled,G)):
    rest=set(enabled)-set(case_g)
    for case_r in list(combinations(rest,R)):
        answer=max(answer,bfs(case_g,case_r))

print(answer)