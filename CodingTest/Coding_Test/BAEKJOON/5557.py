import sys

input=sys.stdin.readline

N=int(input())

arr=list(map(int,input().split()))

answer=0
dp=[dict() for _ in range(N)]

def dfs(index,mid):
    global answer
    if mid in dp[index]:
        return dp[index][mid]
    if index==N-1:
        if mid==arr[N-1]:
            dp[index][mid]=1
        else:
            dp[index][mid]=0
        return dp[index][mid]
    if mid<0 or mid>20:
        dp[index][mid]=0
        return dp[index][mid]
    dp[index][mid]=0
    dp[index][mid]+=dfs(index+1,mid+arr[index])
    dp[index][mid]+=dfs(index+1,mid-arr[index])
    return dp[index][mid]

print(dfs(1,arr[0]))
