import sys
from collections import deque

input=sys.stdin.readline

dx=[-2,-2,0,0,2,2]
dy=[-1,1,-2,2,-1,1]

N=int(input())
r1,c1,r2,c2=map(int,input().split())

visited=[[-1]*N for _ in range(N)]

def bfs(r,c):
    global visited
    q=deque()
    q.append((r,c))
    visited[r][c]=0
    while q:
        now=q.popleft()
        for i in range(6):
            nx=now[0]+dx[i]
            ny=now[1]+dy[i]
            if nx<0 or ny<0 or nx>=N or ny>=N:
                continue
            if visited[nx][ny]!=-1:
                continue
            q.append((nx,ny))
            visited[nx][ny]=visited[now[0]][now[1]]+1

bfs(r1,c1)
print(visited[r2][c2])    