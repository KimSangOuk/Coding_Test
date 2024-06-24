# 풀이시간 5분 시간제한 2초 메모리제한 128MB
# 1회차 정답
# 특정수가 특정수로 규칙에 따라 돌아오는 사이클의 길이를 구하는 문제.

count=0
n=input()
target=int(n)

while True:
  if int(n)<10:
    n="0"+n
  first=n[0]
  second=n[-1]
  add_value=str(int(first)+int(second))[-1]
  count+=1
  # print(first,second,add_value)

  n=second+add_value
  
  if target==int(n):
    break

print(count)