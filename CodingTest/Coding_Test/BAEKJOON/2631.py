import sys
input=sys.stdin.readline

N=int(input())

arr=[]
for i in range(N):
    arr.append(int(input()))

dp=[1]*(N)

for i in range(N):
    for j in range(0,i):
        if arr[i]>arr[j]:
            dp[i]=max(dp[j]+1,dp[i])

print(N-max(dp))