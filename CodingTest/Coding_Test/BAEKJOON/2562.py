# 풀이시간 5분 시간제한 1초 메모리제한 128MB
# 1회차 정답
# 최댓값과 몇번째 수인지 구하는 문제.

n=9
max_index=-1
max_value=-1
for i in range(1,n+1):
  now=int(input())
  if max_value<now:
    max_index=i
    max_value=now

print(max_value)
print(max_index)