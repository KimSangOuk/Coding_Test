def solve():
  n = int(input())  # 동전 종류의 수
  coinsType = list(map(int, input().split()))  # 동전 종류
  m = int(input())  # 목표 금액

  # dp 배열 초기화: dp[i]는 금액 i를 만들 수 있는 경우의 수를 저장
  dp = [0] * (m + 1)
  dp[0] = 1  # 금액 0을 만들 수 있는 경우의 수는 1 (동전 하나도 사용하지 않는 경우)

  # 각 동전을 사용하여 dp 배열 갱신
  for coin in coinsType:
      for i in range(coin, m + 1):
          dp[i] += dp[i - coin]

  # dp[m]에 목표 금액을 만들 수 있는 경우의 수가 저장됨
  print(dp[m])

# 여러 테스트 케이스 처리
for _ in range(int(input())):
  solve()