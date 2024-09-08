n=int(input())

s="moo"
dp=[0]
dp.append(3)
index=1
while True:
    dp.append(dp[index]+1+index+2+dp[index])
    if dp[-1]>=n:
        break
    index+=1

nowIndex=len(dp)-1
while True:
    if nowIndex==0:
        print(s[n-1])
        break
    if dp[nowIndex-1]<n<=nowIndex+2+dp[nowIndex-1]:
        if n==dp[nowIndex-1]+1:
            print('m')
            break
        else:
            print('o')
            break
    if dp[nowIndex-1]<n:                                                 
        n-=nowIndex+2+dp[nowIndex-1]
    nowIndex-=1