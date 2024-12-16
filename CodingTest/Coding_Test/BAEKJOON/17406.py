import sys
import copy
from collections import deque

N,M,K=map(int,input().split())

dx=[0,1,0,-1]
dy=[1,0,-1,0]

board=[list(map(int,input().split())) for _ in range(N)]

opers=[]
for _ in range(K):
    opers.append(tuple(map(int,input().split())))

def rotate(board,oper):
    r,c,s=oper
    new_board=[[0]*(2*s+1) for _ in range(2*s+1)]
    for i in range(2*s+1):
        for j in range(2*s+1):
            new_board[i][j]=board[r-s-1+i][c-s-1+j]

    rotate_board=[[0]*(2*s+1) for _ in range(2*s+1)]

    for stage in range(s+1):
        q=deque()
        q.append((stage,stage))
        visitedBoard=[[False]*(2*(s-stage)+1) for _ in range(2*(s-stage)+1)]
        traceList=deque([new_board[stage][stage]])
        visitedBoard[0][0]=True
        cnt=0
        d=0
        while q:
            now=q.popleft()
            nx=now[0]+dx[d]
            ny=now[1]+dy[d]
            if nx==stage and ny==stage:
                break
            if nx<stage or ny<stage or nx>=stage+2*(s-stage)+1 or ny>=stage+2*(s-stage)+1:
                d=(d+1)%4
                cnt+=1
                if cnt==4:
                    break
                q.append(now)
                continue
            traceList.append(new_board[nx][ny])
            q.append((nx,ny))
        traceList.appendleft(traceList.pop())
        q=deque()
        q.append((stage,stage))
        rotate_board[stage][stage]=traceList.popleft()
        d=0
        cnt=0
        while q and traceList:
            now=q.popleft()
            nx=now[0]+dx[d]
            ny=now[1]+dy[d]
            if nx<stage or ny<stage or nx>=stage+2*(s-stage)+1 or ny>=stage+2*(s-stage)+1:
                d=(d+1)%4
                cnt+=1
                if cnt==4:
                    break
                q.append(now)
                continue
            value=traceList.popleft()
            rotate_board[nx][ny]=value
            q.append((nx,ny))

    result_board=copy.deepcopy(board)
    for i in range(2*s+1):
        for j in range(2*s+1):
            result_board[r-s-1+i][c-s-1+j]=rotate_board[i][j]

    return result_board

def dfs(deep,board,visited):
    global answer,opers
    if deep==K:
        for i in range(N):
            answer=min(answer,sum(board[i]))
        return
    for i in range(K):
        if not visited&(1<<i):
            tmp=copy.deepcopy(board)
            tmp=rotate(tmp,opers[i])
            dfs(deep+1,tmp,visited|(1<<i))

answer=1e9
dfs(0,board,0)        
print(answer)