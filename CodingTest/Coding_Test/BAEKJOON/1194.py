from collections import deque
import copy

dx=[0,0,-1,1]
dy=[-1,1,0,0]
n,m=map(int,input().split())


board=[]
start=0
for i in range(n):
    arr=list(input())
    for j in range(m):
        if arr[j]=='0':
            start=(i,j)
    board.append(arr)

def bfs(board,start):
    key_value=[0]*6
    visited=dict()
    visited[tuple(key_value)]=[[-1]*m for _ in range(n)]
    q=deque()
    visited[tuple(key_value)][start[0]][start[1]]=0
    q.append((key_value,start[0],start[1]))
    while q:
        key_list,x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            if board[nx][ny]=='#':
                continue
            if visited[tuple(key_list)][nx][ny]!=-1:
                continue
            if ord('A')<=ord(board[nx][ny])<=ord('F') and key_list[ord(board[nx][ny])-ord('A')]==0 :
                continue
            if board[nx][ny]=='1':
                return visited[tuple(key_list)][x][y]+1
            if ord('a')<=ord(board[nx][ny])<=ord('f') and key_list[ord(board[nx][ny])-ord('a')]!=1:
                tmp_list=copy.deepcopy(key_list)
                tmp_list[ord(board[nx][ny])-ord('a')]=1
                if tuple(tmp_list) not in visited:
                    visited[tuple(tmp_list)]=[[-1]*m for _ in range(n)]
                visited[tuple(tmp_list)][nx][ny]=visited[tuple(key_list)][x][y]+1
                q.append((tmp_list,nx,ny))
            visited[tuple(key_list)][nx][ny]=visited[tuple(key_list)][x][y]+1
            q.append((key_list,nx,ny))
    return -1


ans=bfs(board,start)



print(ans)


