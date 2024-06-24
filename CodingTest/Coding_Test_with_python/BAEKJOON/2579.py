# 풀이시간 15분 시간제한 1초 메모리제한 128MB
# 1회차 정답
# 계단이 300이하이기 때문에 메모리는 문제가 없고 앞에서부터 따졌을 때, 현재 계단의 상태를 점화식으로 나타낼 수 있기 때문에 다이나믹 프로그래밍으로 접근할 수 있다. 현재의 계단이 i번째 계단이라고 하고, dp가 현재 계단에서의 최댓값이라고 한다면, dp[i]=max(dp[i-2],dp[i-3]+array[i-1])+array[i]이다. 즉, 현재 계단까지의 최댓값은 현재 계단의 값에다가 두번째 전 계단까지의 최댓값이나 직전계단의 값+세번째 계단까지의 최댓값을 더한 값 중 큰 숫자이다.

n=int(input())

array=[]

for _ in range(n):
  array.append(int(input()))

dp=[0]*(n+1)
if n>=1:
  dp[1]=array[0]
if n>=2:
  dp[2]=array[0]+array[1]

for i in range(3,n+1):
  dp[i]=max(dp[i-2],dp[i-3]+array[i-2])+array[i-1]

# print(dp)
print(dp[n])