# 풀이시간 15분 시간제한 2초 메모리제한 128MB
# 1회차 정답
# 모음과 자음을 서로 불리한 다음 갯수의 모음과 자음 비율을 조건에 따라 맞춘 다음 모든 케이스를 나누고, 그 케이스에 따라 모음과 자음중에서 선택하는 또 모든 케이스를 결과에 넣는 문제이다. 완전 탐색문제라고 할 수 있다.

from itertools import combinations

l,c=map(int,input().split())
alpha=list(map(str,input().split()))
default_mo=set(['a','e','i','o','u'])
mo=[]
ja=[]
for a in alpha:
  if a in default_mo:
    mo.append(a)
  else:
    ja.append(a)

moja=[]
for i in range(1,len(mo)+1):
  if l-i<2:
    break
  moja.append((i,l-i))

result=[]
for m,j in moja:
  for case in list(combinations(mo,m)):
    for case2 in list(combinations(ja,j)):
      result.append(sorted(case+case2))

result.sort()
for i in result:
  print(''.join(i))