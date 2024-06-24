# 풀이시간 5분 시간제한 1초 메모리제한 256MB
# 1회차 정답
# 단순히 tc를 입력받은 후 그 수만큼 a,b를 입력받아 출력하는 구현 문제.

for _ in range(int(input())):
  a,b=map(int,input().split())
  print(a+b)