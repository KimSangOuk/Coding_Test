# 풀이시간 3분 시간제한 1초 메모리제한 128MB
# 1회차 정답
# 9개중 7개의 수를 고르는 케이스를 전부 탐색해서 합이 100이되는 경우를 출력하는 완전탐색, 브루트포스 알고리즘 문제이다.

from itertools import combinations

array=[]
for _ in range(9):
  array.append(int(input()))

for case in list(combinations(array,7)):
  if sum(case)==100:
    for i in case:
      print(i)
    break