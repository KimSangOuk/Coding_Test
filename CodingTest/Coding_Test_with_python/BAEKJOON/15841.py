# 풀이시간 5분 시간제한 2초 메모리제한 512MB
# 1회차 정답
# 피보나치 수열을 이루고 있기 때문에 다이나믹 프로그래밍, 바텀업 방식으로 기록하고 출력한다.

dp=[0]*(490+1)
dp[1]=1
dp[2]=1

for i in range(3,491):
  dp[i]=dp[i-1]+dp[i-2]

while True:
  n=int(input())
  if n==-1:
    break
  print("Hour "+str(n)+": "+str(dp[n])+" cow(s) affected")
  