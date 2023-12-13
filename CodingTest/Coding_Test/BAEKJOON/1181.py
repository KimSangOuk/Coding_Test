# 풀이시간 10분 시간제한 2초 메모리제한 256MB
# 1회차 정답
# 단순히 문자열을 배열하는 문제인 줄 알았으나 중복제거가 있길래 set로 한번 받은 후 정렬 시켜주었다.

n=int(input())

arr=set()
for _ in range(n):
  s=input()
  arr.add(s)

arr=list(arr)
arr.sort(key=lambda x:(len(x),x))

for i in range(len(arr)):
  print(arr[i])