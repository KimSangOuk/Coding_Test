# 풀이시간 10분 시간제한 0.15초 메모리제한 128MB
# 1회차 정답
# 횟수를 구하는 문제이기 때문에 그 전에 될 수 있는 값들 중 최소 값에 1을 더해서 현재의 값을 더하는 문제이다. 즉, 전의 값이 현재의 값에 계속해서 영향을 주는 문제인 다이나믹 프로그래밍으로 풀 수 있다.

n=int(input())

d=[0]*(n+1)
for i in range(2,n+1):
  one=1e9
  two=1e9
  if i%2==0:
    one=d[i//2]
  if i%3==0:
    two=d[i//3]
  d[i]=min(one,two,d[i-1])+1

print(d[n])