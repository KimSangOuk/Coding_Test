# 풀이시간 30분 시간제한 0.5초 메모리제한 128MB
# 1회차 정답
# 먼저 시간복잡도가 0.5초 이기 때문에 연산이 약 1000만회 이하로 이루어지는게 적절하다. 각 집을 칠하면서 현재의 집에서 칠해진 집은 전의 집에서 칠해지지 않기 때문에, 현재의 집에서 칠해지는 최소 값은 전의 나머지 두 색에서 칠해진 값중 최소값에서 현재의 집에서의 최솟값을 더하는것과 같다. 그렇기 때문에 현재의 답이 부분해의 답으로 이루어지기 때문에 각 색별로 구하고 마지막 집에서는 3가지로 나누어지기 때문에 그 중 가장 작은 값을 출력하면 된다
n=int(input())

dp=[[0]*3 for _ in range(n)]

colors=[]
for i in range(n):
  colors.append(list(map(int,input().split())))

dp[0][0]=colors[0][0]
dp[0][1]=colors[0][1]
dp[0][2]=colors[0][2]

for i in range(1,n):
  for j in range(3):
    min_value=int(1e9)
    for k in range(3):
      if j!=k:
        min_value=min(min_value,dp[i-1][k])
    dp[i][j]=min_value+colors[i][j]

print(min(dp[n-1][0],dp[n-1][1],dp[n-1][2]))
