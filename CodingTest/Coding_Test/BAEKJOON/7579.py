N,M=map(int,input().split())
A=list(map(int,input().split()))
m=list(map(int,input().split()))
result=1e9
A=[0]+A
m=[0]+m

dp=[[0]*(sum(m)+1) for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(0,sum(m)+1):
        nowWeight=A[i]
        nowCost=m[i]
        if j<nowCost:
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j]=max(dp[i-1][j-nowCost]+nowWeight,dp[i-1][j])
        if dp[i][j]>=M:
            result=min(result,j)
print(result)    
