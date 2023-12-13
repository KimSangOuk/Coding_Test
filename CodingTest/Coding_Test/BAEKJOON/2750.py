# 풀이시간 1분 시간제한 1초 메모리제한 128MB
# 1회차 정답
# 단순 정렬해서 출력하는 문제이다.

n=int(input())
arr=[]
for i in range(n):
  arr.append(int(input()))

arr.sort()
for i in range(n):
  print(arr[i])