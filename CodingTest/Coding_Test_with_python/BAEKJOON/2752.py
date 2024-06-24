# 풀이시간 3분 시간제한 1초 메모리제한 128MB
# 1회차 정답
# 단순히 수를 받아서 정렬한 결과를 출력하면 되는 문제이다.

array=list(map(int,input().split()))
array.sort()
for i in range(len(array)):
  print(array[i],end=' ')