import sys
input=sys.stdin.readline

s1=list(input())[:-1]
s2=list(input())[:]
dp=[[0]*(len(s2)+1) for _ in range(len(s1)+1)]

answer=""
for i in range(1,len(s1)+1):
    for j in range(1,len(s2)+1):
        if s1[i-1]==s2[j-1]:
            dp[i][j]=dp[i-1][j-1]+1
        else:
            dp[i][j]=max(dp[i-1][j],dp[i][j-1])

print(dp[len(s1)][len(s2)])
longest=dp[len(s1)][len(s2)]
j=len(s2)
prev=len(s2)
for i in range(len(s1),-1,-1):
    find=False
    while j>=0:
        if s1[i-1]==s2[j-1]:
            if dp[i][j]==longest:
                if dp[i-1][j]==dp[i][j-1] and dp[i-1][j]==dp[i-1][j-1]:
                    answer=s1[i-1]+answer
                    longest-=1
                    prev=j-1
                    j=j-1
                    find=True
                    break
        j-=1
    if not find:
        j=prev

print(answer)