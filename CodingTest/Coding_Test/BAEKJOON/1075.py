# 풀이시간 5분 시간제한 2초 메모리제한 128MB
# 1회차 정답
# 단순하게 현재의 끝자리가 0~99까지 전체 탐색하면서 각 수가 나누어떨어지는 최소의 수인 경우를 구하면 되는 문제이다. 완전탐색 알고리즘이라고 할 수 있다.

n=int(input())
f=int(input())

start=(n//100)*100
end=start+100

for i in range(start,end):
  if i%f==0:
    print(str(i)[-2:])
    break