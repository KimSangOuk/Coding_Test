# 풀이시간 3분 시간제한 1초 메모리제한 256MB
# 1회차 정답
# 중복을 집합으로 제거하고 정렬하면 되는 문제이다.

n=int(input())
array=list(set(list(map(int,input().split()))))
array.sort()

for i in range(len(array)):
  print(array[i],end=' ')