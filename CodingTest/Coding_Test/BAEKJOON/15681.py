import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**5)

n,r,q=map(int,input().split())

dp=[0]*(n+1)

graph=[[] for _ in range(n+1)]
for i in range(n-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(node):
    sum=1
    for i in graph[node]:
        if visited[i]:
            continue
        visited[i]=True
        sum+=dfs(i)     
    dp[node]=sum
    return sum

visited=[False]*(n+1)
visited[r]=True
dfs(r)
for _ in range(q):
    print(dp[int(input())])