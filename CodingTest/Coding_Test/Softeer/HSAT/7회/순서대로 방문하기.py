from collections import deque

n,m=map(int,input().split())
board=[list(map(int,input().split())) for _ in range(n)]

dx=[0,0,-1,1]
dy=[-1,1,0,0]

def dfs(now,path,point):
    global endPoint,answer,board
    if now==endPoint and len(point)==0:
        answer+=1
        return
    for i in range(4):
        nx=now[0]+dx[i]
        ny=now[1]+dy[i]
        if nx<0 or ny<0 or nx>=n or ny>=n:
            continue
        if board[nx][ny]==1:
            continue
        if (nx,ny) in path:
            continue
        path.append((nx,ny))
        tmp=-1
        if len(point)>0 and point[0]==(nx,ny):
            tmp=point.popleft()
        dfs((nx,ny),path,point)
        if tmp!=-1:
            point.appendleft(tmp)
        path.pop()
arr=list(map(int,input().split()))
startPoint=(arr[0]-1,arr[1]-1)
point=deque()
for _ in range(m-2):
    x,y=map(int,input().split())
    point.append((x-1,y-1))
arr=list(map(int,input().split()))
endPoint=(arr[0]-1,arr[1]-1)
answer=0
path=[startPoint]
dfs(startPoint,path,point)
print(answer)