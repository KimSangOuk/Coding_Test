n=int(input())
dp=[0]*n
edges=[]
for i in range(n):
    a,b=map(int,input().split())
    edges.append((a,b))
    dp[i]=1

edges.sort()
for i in range(n):
    for j in range(0,i):
        if edges[i][1]>edges[j][1]:
            dp[i]=max(dp[j]+1,dp[i])

print(n-max(dp))