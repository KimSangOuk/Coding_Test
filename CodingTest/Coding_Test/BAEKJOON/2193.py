# 풀이시간 15분 시간제한 2초 메모리제한 128MB
# 1회차 정답
# 각 이친수는 전의 수에다가 0을 더하는 방법과 전전수에 01을 붙이는 방법이 있다. 이러한 형태는 파보나치 수열을 이루기도 한다. 전체해가 부분해의 합으로 이루어지기 때문에 다이나믹 프로그래밍으로 풀어주면 된다.

n=int(input())

dp=[0]*(90+1)
dp[1]=1
dp[2]=1
for i in range(3,91):
  dp[i]=dp[i-1]+dp[i-2]

print(dp[n])
