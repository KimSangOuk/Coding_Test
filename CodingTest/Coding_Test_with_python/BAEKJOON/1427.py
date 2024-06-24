# 풀이시간 5분 시간제한 2초 메모리제한 128MB
# 1회차 정답
# 단순히 숫자를 내림차순 정렬하면 되는 문제이다. 길이가 길어야 10자리이기 때문에 충분히 가능하다.

n=int(input())

arr=[]
for s in str(n):
  arr.append(int(s))

arr.sort(reverse=True)
for s in arr:
  print(s,end='')