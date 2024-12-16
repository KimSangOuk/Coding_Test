import sys

input=sys.stdin.readline

n=int(input())
arr=list(map(int,input().split()))

dp=arr[:]
sum=[0]*n

for i in range(n):
    max_value=0
    for j in range(i):
        if arr[j]<arr[i]:
            max_value=max(max_value,dp[j])
    dp[i]+=max_value

print(max(dp))
