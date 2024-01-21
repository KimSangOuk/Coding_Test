# 풀이시간 5분 시간제한 1초 메모리제한 1024MB
# 1회차 정답
# 피보나치 수열을 만들어서 다이나믹 프로그래밍 방식으로 바텀업으로 쌓아올려서 풀었다.

dp=[0]*46
dp[0]=1
dp[1]=1
for i in range(2,46):
  dp[i]=dp[i-1]+dp[i-2]

for tc in range(int(input())):
  n=int(input())
  print(dp[n])