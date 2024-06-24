# 풀이시간 4분 시간제한 2초 메모리제한 256MB
# 1회차 정답
# 각 집합에 다른 집합에 있는 수들이 있는지 확인하는 문제이다. 이 때, 각 수가 있는지만 확인하면 되는데, 데이터의 크기가 100만이기 때문에 O(N)을 넘지 않는것이 좋다. 그렇기 데이터를 확인할 수들을 집합으로 받고 이를 in 으로 확인하면 O(N)으로 간단히 확인할 수 있기 때문에 가능하다.

for tc in range(int(input())):
  n=int(input())
  array1=set(map(int,input().split()))
  m=int(input())
  array2=list(map(int,input().split()))
  for k in array2:
    if k in array1:
      print(1)
    else:
      print(0)