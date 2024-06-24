# 풀이시간 5분 시간제한 2초 메모리제한 128MB
# 1회차 정답
# 단순하게 최소 수인 666부터 전부 탐색해 나가는 브루트포스 알고리즘이다. 숫자가 아무리커져도 10,000,000에 O(N)이기 때문에 가능하다.

n=int(input())

start=666
while True:
  if '666' in str(start):
    n-=1

  if n==0:
    break

  start+=1
print(start)