# 풀이시간 10분 시간제한 1초 메모리제한 128MB
# 1회차 정답
# 딱 보고 조합을 사용해서 풀면 되겠다 이 생각이 들엇는데 조합 자체가 전체 경우의 수를 건드리는 완전 조합, 브루트포스 알고리즘이다.

from itertools import combinations

n,m=map(int,input().split())
arr=list(map(int,input().split()))

result=0
new_arr=list(combinations(arr,3))
for a,b,c in new_arr:
  if a+b+c<=m:
    result=max(a+b+c,result)

print(result)