# 풀이시간 10분 시간제한 2초 메모리제한 128MB
# 1회차 풀이
# 단순히 가장 작은 자연수부터 순서대로 더해서 주어진 크기가 되기 전까지의 수를 모두 더하면되는 문제이다. 그러면 수들의 서로 다른 합이 목표의 수가 될 때, 이루는 수중 가장 큰 수가 몇인지 알 수 있다. 이 때, 시간복잡도는 while문이 돌아가는 연산의 횟수인데, s의 크기가 약 40억 이지만 1부터 N까지 더했을 때 약 N^2의 N에 해당하는 연산이 나오므로 많아도 N이 10만 밑인걸 알 수 있다.

s=int(input())

n=1
result=n
while True:
  if s<result:
    break
  n+=1
  result+=n
  

print(n-1)