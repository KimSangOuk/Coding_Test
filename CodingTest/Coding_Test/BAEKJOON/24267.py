# 풀이시간 5분 시간제한 1초 메모리제한 512MB
# 1회차 정답
# 주어진 함수의 연산 횟수와 시간복잡도의 다항 차수를 구하는 문제이다.

n=int(input())
dp=[0]*(n-1)
for i in range(1,n-1):
    dp[i]=dp[i-1]+i

answer=0
for i in range(1,n-1):
    answer+=dp[i]
print(answer)
print(3)