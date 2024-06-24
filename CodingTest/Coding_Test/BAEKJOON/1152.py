# 풀이시간 5분 시간제한 2초 메모리제한 128MB
# 1회차 정답
# 각 단어의 수를 세는 문제이다.

arr=input().strip()
array=list(arr.split(" "))
if len(array)==1 and len(array[0])==0:
  print(0)
else:
  print(len(array))