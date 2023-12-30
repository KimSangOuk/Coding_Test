# 풀이시간 5분 시간제한 2초 메모리제한 128MB
# 1회차 정답
# 단순하게 9개 중 7개의 합이 100이 되는 수를 전부 따지는 브루트 포스 알고리즘이다.

from itertools import combinations

arr=[]
for _ in range(9):
  arr.append(int(input()))

cases=list(combinations(arr,7))
for case in cases:
  if sum(case)==100:
    answer_list=list(case)
    break

answer_list.sort()
for i in answer_list:
  print(i)