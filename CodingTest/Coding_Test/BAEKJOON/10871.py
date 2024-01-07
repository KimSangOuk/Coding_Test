# 풀이시간 5분 시간제한 1초 메모리제한 256MB
# 1회차 정답
# 단순하게 특정 수보다 작은 수를 찾아 출력하는 구현 문제.

n,x=map(int,input().split())
array=list(map(int,input().split()))
for i in array:
  if i<x:
    print(i,end=' ')