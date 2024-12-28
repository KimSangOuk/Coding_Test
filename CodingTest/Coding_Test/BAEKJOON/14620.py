import sys
import copy
input=sys.stdin.readline

N=int(input())

dx=[0,0,-1,1]
dy=[-1,1,0,0]

costs=[list(map(int,input().split())) for _ in range(N)]
answer=200*3*5

visited=[[False]*N for _ in range(N)]

def dfs(cnt,cost,visited):
    global answer
    if cnt==3:
        answer=min(answer,cost)
        return
    for i in range(N):
        for j in range(N):
            if visited[i][j]:
                continue
            out=False
            plusCost=costs[i][j]
            copyVisited=copy.deepcopy(visited)
            copyVisited[i][j]=True
            for k in range(4):
                nx=i+dx[k]
                ny=j+dy[k]
                if nx<0 or ny<0 or nx>=N or ny>=N:
                    out=True
                    break
                if visited[nx][ny]:
                    out=True
                    break
                plusCost+=costs[nx][ny]
                copyVisited[nx][ny]=True
            if out:
                continue
            dfs(cnt+1,cost+plusCost,copyVisited)
dfs(0,0,visited)
print(answer)