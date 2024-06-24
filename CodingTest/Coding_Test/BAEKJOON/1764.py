# 풀이시간 5분 시간제한 2초 메모리제한 256MB
# 1회차 정답
# 단순히 두 배열의 교집합을 구해서 정렬한 후 출력하면 되는 문제이다. 전부 교집합에 속하는 경우 데이터의 크기가 최대 500,000이므로 2초 동안 O(NlogN)으로 가능하다.

n,m=map(int,input().split())

arr1=[]
arr2=[]
for _ in range(n):
  arr1.append(input())
for _ in range(m):
  arr2.append(input())

answer=list(set(arr1)&set(arr2))
answer.sort()

print(len(answer))
for k in answer:
  print(k)