# 풀이시간 5분 시간제한 1초 메모리제한 512MB
# 1회차 정답
# 재귀함수로 만든 파보나치 수열의 연산 횟수는 피보나치 수열과 연산횟수의 증가량이 같다. 그리고 다이나믹 프로그래밍으로 푼 횟수는 1,2를 재외한 n-2와 같다.

n=int(input())

answer1=0
answer2=n-2

dp=[0]*(n+1)
dp[1]=1
dp[2]=1
for i in range(3,n+1):
  dp[i]=dp[i-1]+dp[i-2]

print(dp[n],answer2)