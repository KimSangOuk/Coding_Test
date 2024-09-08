import sys
sys.setrecursionlimit(1000001)
input=sys.stdin.readline

n=int(input())
graph=[[] for _ in range(n+1)]

for _ in range(n-1):
    u,v=map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

dp=[-1]*(n+1)

def dfs(v):
    noChild=True
    for i in graph[v]:
        if not visited[i]:
            noChild=False
            break
    if noChild:
        dp[v]=0
        return 0
    if dp[v]!=-1:
        return dp[v]
    dp[v]=0
    for i in graph[v]:
        if not visited[i]:
            visited[i]=True
            k=dfs(i)
            if k==0:
                dp[v]=1
    return dp[v]

visited=[False]*(n+1)
visited[1]=True
dfs(1)
print(sum(dp[1:]))