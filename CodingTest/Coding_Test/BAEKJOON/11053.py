# 풀이시간 10분 시간제한 1초 메모리제한 256MB
# 1회차 정답
# 가장 긴 증가하는 부분 수열(LIS) 알고리즘의 대표적 예시이다. 가장 긴 증가하는 부분 수열은 0<=j<i일 때, array[i]>array[j]라면, dp[i]=max(dp[i],dp[j]+1)이 되는 점화식을 가지고 있다. 즉 자기보다 작은 수 중에 최댓값 중에서 +1을 한 값이 현재의 값이 되는 것이다.

n=int(input())

array=list(map(int,input().split()))

dp=[1]*(n+1)

for i in range(1,n+1):
  for j in range(1,i):
    if array[i-1]>array[j-1]:
      dp[i]=max(dp[i],dp[j]+1)

# print(dp)

print(max(dp))