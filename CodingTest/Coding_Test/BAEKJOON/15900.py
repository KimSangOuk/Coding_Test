import sys

sys.setrecursionlimit(500000) 
input=sys.stdin.readline

N=int(input())
graph=[[] for _ in range(N+1)]

for _ in range(N-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited=[False]*(N+1)
answer=0

def dfs(v,layer,visited):
    global answer
    visited[v]=True
    enabled=False
    for i in graph[v]:
        if not visited[i]:
            dfs(i,layer+1,visited)
            enabled=True
    if not enabled:
        answer+=layer

dfs(1,0,visited)
if answer%2==0:
    print("No")
else:
    print("Yes")
