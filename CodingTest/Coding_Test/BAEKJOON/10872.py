# 풀이시간 5분 시간제한 1초 메모리제한 256MB
# 1회차 정답
# 팩토리얼을 구하는 문제이다. 전의 것을 저장해서 현재의 답은 전의 해의 답으로 만들 수 있기 때문에 다이나믹 프로그래밍으로 풀었다.

n=int(input())

dp=[0]*(n+1)
dp[0]=1

for i in range(1,n+1):
    dp[i]=i*dp[i-1]

print(dp[n])