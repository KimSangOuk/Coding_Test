# 풀이시간 5분 시간제한 1초 메모리제한 256MB
# 1회차 정답
# 단순하게 리스트를 정렬하는 문제이다. 데이터 양이 100,000이기 때문에 O(NlogN)인 sort 라이브러리를 사용했다.

n=int(input())

arr=[]
for _ in range(n):
  x,y=map(int,input().split())
  arr.append((x,y))

arr.sort()

for x,y in arr:
  print(x,y)