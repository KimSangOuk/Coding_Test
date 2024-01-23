# 이것이 취업을 위한 코딩테스트다 part03 '34. 병사 배치하기'와 동일

n=int(input())
array=list(map(int,input().split()))
array.reverse()

dp=[1]*(n)

for i in range(0,n):
    max_value=0
    for j in range(i):
        if array[j]<array[i]:
            dp[i]=max(dp[i],dp[j]+1)
print(n-max(dp))