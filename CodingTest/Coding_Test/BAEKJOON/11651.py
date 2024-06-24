# 풀이시간 5분 시간제한 1초 메모리제한 256MB
# 1회차 정답
# 단순히 기준에 따라 정렬하는 문제이다.

n=int(input())
arr=[]
for _ in range(n):
  x,y=map(int,input().split())
  arr.append((x,y))

arr.sort(key=lambda x:(x[1],x[0]))

for x,y in arr:
  print(x,y)