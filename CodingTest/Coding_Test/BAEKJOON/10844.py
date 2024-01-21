# 풀이시간 50분 시간제한 1초 메모리제한 256MB
# 1회차 정답
# 각 숫자의 갯수는 전의 마지막 자리의 숫자에 영향을 받기 때문에 전의 해로 현재의 해를 구하는 다이나믹 프로그래밍을 생각해 볼 수 있다. 이 때, 각 숫자는 전의 마지막 숫자의 양 사이드의 있는 숫자에서 나오기 때문에 각 사이드를 차례로 지나면서 더해주면 되고 마지막 해의 경우는 그 숫자들을 전부 더해주면 된다.

n=int(input())

dp=[[0]*10 for _ in range(n+1)]
for i in range(1,10):
  dp[1][i]=1
for i in range(2,n+1):
  for j in range(10):
    if j==0:
      left=0
      right=dp[i-1][j+1]
    elif j==9:
      right=0
      left=dp[i-1][j-1]
    else:
      left=dp[i-1][j-1]
      right=dp[i-1][j+1]
    
    dp[i][j]=left+right

# print(dp)
print(sum(dp[n])%int(1e9))
  