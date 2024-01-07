# 풀이시간 5분 시간제한 1초 메모리제한 512MB
# 1회차 정답
# 각 합을 출력하는 간단한 문제.

import sys
for i in range(int(input())):
  a,b=map(int,sys.stdin.readline().split())
  print(a+b)