# 풀이시간 5분 시간제한 3초 메모리제한 512MB
# 1회차 정답
# 단순히 받는 번호를 추가적으로 데이터로 받아서 나이, 번호 순으로 정렬시킨다음 출력을 나이, 이름으로 출력하면 되는 문제이다. 데이터의 양이 최대 100,000이므로 퀵 정렬을 사용하였다.

n=int(input())

arr=[]
for i in range(n):
  age,name=input().split()
  arr.append((int(age),i,name))

arr.sort(key=lambda x:(x[0],x[1]))
for age,num,name in arr:
  print(age,name)