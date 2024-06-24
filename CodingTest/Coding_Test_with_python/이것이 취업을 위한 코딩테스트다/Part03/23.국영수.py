# 풀이시간 10분/20분 시간제한 1초 메모리제한 256MB
# 1회차 정답
# 단순 정렬하는 문제이다. 데이터를 보았을 때, 100,000이기 때문에 O(NlogN)을 사용하면 딱 맞아 떨어진다. 기존 라이브러리의 정렬 함수를 사용했다.

n=int(input())
arr=[]
for _ in range(n):
  a=list(input().split())
  arr.append((a[0],int(a[1]),int(a[2]),int(a[3])))

arr.sort(key=lambda x:(-x[1],x[2],-x[3],x[0]))
for i in range(n):
  print(arr[i][0],)