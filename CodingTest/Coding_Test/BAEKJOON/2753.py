# 풀이시간 5분 시간제한 1초 메모리제한 128MB
# 1회차 정답
# 단순히 주어진 조건이 성립하면 1 아니면 0을 출력하는 구현 문제.

y=int(input())

if y%4==0 and y%100!=0 or y%400==0:
  print(1)
else:
  print(0)