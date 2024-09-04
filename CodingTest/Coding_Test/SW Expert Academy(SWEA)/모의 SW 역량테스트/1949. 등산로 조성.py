from collections import deque

dx=[0,0,-1,1]
dy=[-1,1,0,0]

def dfs(x,y,deep):
    global longestLoad
    longestLoad=max(longestLoad,deep)
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx<0 or ny<0 or nx>=N or ny>=N:
            continue
        if board[nx][ny]>=board[x][y]:
            continue
        dfs(nx,ny,deep+1)

for tc in range(1,int(input())+1):
    N,K=map(int,input().split())
    maxH=0
    maxHList=[]
    board=[]
    for i in range(N):
        arr=list(map(int,input().split()))
        for j in range(N):
            if arr[j]>maxH:
                maxH=arr[j]
                maxHList=[]
                maxHList.append((i,j))
            elif arr[j]==maxH:
                maxHList.append((i,j))
        board.append(arr)
    longestLoad=1
    for i in range(N):
        for j in range(N):
            for k in range(0,K+1):
                board[i][j]-=k
                for x,y in maxHList:
                    dfs(x,y,1)

                board[i][j]+=k
    print("#"+str(tc)+" "+str(longestLoad))
