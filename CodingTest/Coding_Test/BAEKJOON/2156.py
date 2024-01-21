# 풀이시간 25분 시간제한 2초 메모리제한 256MB
# 1회차 정답
# 현재의 포도주의 최댓값은 다음의 부분해의 합으로 이루어질 수 있다. 두번째 전 잔의 최댓값과 현재 잔 / 세번째 전 잔까지의 최댓값과 현재 잔과 두 번째 전 잔 / 네번째 전 잔을 마시고 현재 전잔과 현재 잔 이렇게 3가지의 방법 중 최댓값이 현재 잔의 최댓값이 될 수 있다. 그렇기에 답은 전에 잔을 마셨으면 현재 잔은 못마실 수 있기 때문에 두가지 답 중 최댓값을 출력하면 된다.

n=int(input())

dp=[0]*(n+1)
array=[]
for i in range(n):
  array.append(int(input()))

array=[0]+array
dp[0]=0
dp[1]=array[1]
if n>=2:
  dp[2]=array[1]+array[2]
if n>=3:
  dp[3]=max(dp[2],array[1]+array[3],array[2]+array[3])

for i in range(4,n+1):
  dp[i]=max(dp[i-4]+array[i]+array[i-1],dp[i-3]+array[i-1]+array[i],dp[i-2]+array[i])

# print(dp)

print(max(dp[n-1],dp[n]))