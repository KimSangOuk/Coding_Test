n=int(input())

dp=[[[-1]*(1024) for _ in range(10)] for _ in range(101)]

def showbit(bit):
    k=""
    for i in range(9,-1,-1):
        if bit&(1<<i):
            k+="1"
        else:
            k+="0"
    return k

def dfs(now,deep,bit):
    if deep==n:
        allExist=True
        for i in range(10):
            if not (bit>>i)&1:
                allExist=False
        if allExist:
            dp[deep][now][bit]=1
            return 1
        dp[deep][now][bit]=0
        return 0
    dp[deep][now][bit]=0
    if now+1<10:
        if dp[deep+1][now+1][bit|1<<(now+1)]!=-1:
            dp[deep][now][bit]+=dp[deep+1][now+1][bit|1<<(now+1)]
        else:
            dp[deep][now][bit]+=dfs(now+1,deep+1,bit|1<<(now+1))
    if now-1>=0:
        if dp[deep+1][now-1][bit|1<<(now-1)]!=-1:
            dp[deep][now][bit]+=dp[deep+1][now-1][bit|1<<(now-1)]
        else:
            dp[deep][now][bit]+=dfs(now-1,deep+1,bit|1<<(now-1))
    return dp[deep][now][bit]

cnt=0
for i in range(1,10):
    cnt+=dfs(i,1,0|1<<i)

print(cnt%1000000000)
