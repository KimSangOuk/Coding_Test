# 풀이시간 5분 시간제한 1초 메모리제한 128MB
# 1회차 정답
# 단순히 별을 출력하는 구현 문제.

n=int(input())
for i in range(1,n+1):
  print(' '*(n-i)+'*'*i)