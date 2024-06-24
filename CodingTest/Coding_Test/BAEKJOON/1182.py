# 풀이시간 7분 시간제한 2초 메모리제한 256MB
# 1회차 정답
# 각 부분수열이 되는 모든 경우를 조합으로 구한 다음, 그 수들의 합이 s가 되는 모든 경우를 탐색하는 완전탐색 문제이다.
# 이때 조합의 공식은 n!/(n-r)!r! 임을 잊지 말자!

from itertools import combinations

n,s=map(int,input().split())
array=list(map(int,input().split()))

count=0
for i in range(1,n+1):
  for case in list(combinations(array,i)):
    if sum(case)==s:
      count+=1

print(count)