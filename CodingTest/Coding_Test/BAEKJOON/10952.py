# 풀이시간 5분 시간제한 1초 메모리제한 256MB
# 1회차 정답
# 단순히 합을 출력하는 구현 문제.

while True:
  a,b=map(int,input().split())
  if a==0 and b==0:
    break
  print(a+b)