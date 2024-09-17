dp=[0]*31
dp[2]=3
n=int(input())

for i in range(4,31):
    if i%2==0:
        dp[i]=dp[i-2]*3
        for j in range(4,i,2):
            dp[i]+=dp[i-j]*2
        dp[i]+=2

print(dp[n])