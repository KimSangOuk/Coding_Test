# 풀이시간 3분 시간제한 1초 메모리제한 256MB
# 1회차 정답
# 두가지 입력을 받아서 그 중 하나를 기준으로 정렬해서 가장 큰 수의 다른 값을 가져오는 문제이다.

for tc in range(int(input())):
  n=int(input())
  array=[]
  for i in range(n):
    name,l=input().split()
    array.append((int(l),name))
  array.sort()
  print(array[-1][1])